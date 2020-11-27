# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from .fangxing_rent import FangxingRentSpider

class FangxingShangpuSpider(CrawlSpider): #继承租房的
    name = 'fangxing_shangpu'
    allowed_domains = ['www.fangstar.com']
    start_urls = ['http://www.fangstar.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
