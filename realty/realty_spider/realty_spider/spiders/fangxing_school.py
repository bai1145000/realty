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
        Rule(LinkExtractor(allow=r'/xuexiao'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/xuexiao/pg\d+$'), follow=True),
    )
    custom_settings = {
        'ITEM_PIPELINES':{'realty_spider.realty_spider.pipelines.FangxingSchoolPipeline':300},
    }
    queryset = FangxingXuexiao.objects.all()
    def parse_item(self, response):
        for i in response.xpath('//ul[@class="house-list fl"]/li'):
            item = FangxingSchoolItems()  
            item['url'] = i.xpath('./a/@href').extract_first()
            item['school'] = i.xpath('./div/h3[@class="title"]/a/text()').extract_first()
            item['region'] = i.xpath('./div/em[1]/span[1]/text()').extract_first()
            item['school_type'] = i.xpath('./div/em[1]/span[2]/text()').extract_first()
            school_nature = i.xpath('./div/em[2]/text()').extract_first()
            item['school_nature'] = school_nature
            item['location'] = i.xpath('./div/em[3]/text()').extract_first()
            yield item
