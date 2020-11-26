# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fangxing.models import FangxingRent
from realty_spider.realty_spider.items import FangxingZufangItems



class FangxingRentSpider(CrawlSpider):
    name = 'fangxing_rent'
    allowed_domains = ['www.fangstar.com']
    start_urls = ['https://www.fangstar.com/zufang']

    rules = (
        # Rule(LinkExtractor(allow=r''), follow=True),
        Rule(LinkExtractor(allow=r'/zufang/[a-z]\w+$'), callback='parse_item', follow=True),#请求list
        Rule(LinkExtractor(allow=r'/zufang/pg\d+$'), follow=True), #翻页请求
    )
    queryset = FangxingRent.objects.all()
    def parse_item(self, response):
        for i in response.xpath('//*[@class = "house-list fl"]/li'):
            item = FangxingZufangItems()
            item['url'] = i.xpath('./a/@href').extract_first()
            item['community'] = i.xpath('./div/em[1]/a/text()').extract_first()
            address = i.xpath('./div/em[2]/span/a/text()').extract()
            item['address'] = address[0] + '-'+ address[1] if len(address)>=2 else address[0]
            total_price =  i.xpath('./div/div/h3/text()').extract_first() + i.xpath('./div/div/h3/span/text()').extract_first()
            item['rent_price'] =  total_price
            publish_time = i.xpath('./div/em[3]/span/text()').extract_first()
            item['publish_time'] = publish_time.split('发')[0] if publish_time else None
            item['house_type'] = i.xpath('./div/em[1]/span[2]/text()').extract_first() 
            # print(i)
            yield item
        
    def parse_details(self, response):
        meta_items = response.meta.get('items')
        item = FangxingZufangItems()
        fx_fields={'房屋用途':'house_usage','装修程度':'house_renovation_type','房屋类型':'house_type',
            '楼梯类型':'stair_type','梯  户 数':'ladder_household_ratio','入住时间':'check_in_time',
            '洗衣机':'is_washing','热水器':'is_fridge','电视','冰箱':'is_fridge
            ','沙发','宽带','天然气','微波炉','电视','热水器','衣柜',
            }
        for i in response.xpath('//ul[@class="house-basic-info"]/li'): #基本信息
            label = i.xpath('./span[@class="label"]/text()').extract_first()
            value = i.xpath('./span[2]/text()').extract_first()
        for i in response.xpath('//div[@class="content"]/div'):

