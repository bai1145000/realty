# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fangxing.models import FangxingXuexiao
from realty_spider.realty_spider.items import FangxingSchoolItems


class FangxingSchoolSpider(CrawlSpider):
    name = 'fangxing_school'
    allowed_domains = ['www.fangstar.com']
    start_urls = ['http://www.fangstar.com/xuexiao/']

    rules = (
        Rule(LinkExtractor(allow=r'/xuexiao/[a-z]\w+$'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/xuexiao/pg\d+$'), follow=True),
    )
    custom_settings = {
        'ITEM_PIPELINES':{
            'realty_spider.realty_spider.pipelines.StringPipeline':300,
            'realty_spider.realty_spider.pipelines.FangxingSchoolPipeline':300,},
    }
    queryset = FangxingXuexiao.objects.all()
    def parse_item(self, response):
        for i in response.xpath('//ul[@class="house-list fl"]/li'):
            item = {}
            item['url'] = i.xpath('./a/@href').extract_first()
            item['school'] = i.xpath('./div/h3[@class="title"]/a/text()').extract_first()
            item['region'] = i.xpath('./div/em[1]/span[1]/text()').extract_first()
            item['school_type'] = i.xpath('./div/em[1]/span[2]/text()').extract_first()
            school_nature = i.xpath('./div/em[2]/text()').extract_first()
            school_nature = school_nature.split('：')[1] if school_nature else None
            item['school_nature'] = school_nature
            location = i.xpath('./div/em[3]/text()').extract_first() 
            item['location'] = location.split('：')[1] if location else None #地址
            yield scrapy.Request(
                url=item['url'],callback=self.parse_details,meta={'item':item}
            )

    def parse_details(self, response):
        meta = response.meta.get('item')
        item = FangxingSchoolItems()
        item['phone_numbers'] = response.xpath('//div[@class="school-pz fangyuan-pz"]/dl[4]/dd/text()').extract_first()
        item['school_url'] = response.xpath('//p[@class="school-website"]/a/@href').extract_first()
        item['pair_school'] = response.xpath('//dl[@class="overflow"]/dd/a/text()').extract_first()
        item.update(meta)
        yield item
        
