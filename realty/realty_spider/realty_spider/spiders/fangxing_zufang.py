# -*- coding: utf-8 -*-
import scrapy


class FangxingZufangSpider(scrapy.Spider):
    name = 'fangxing_zufang'
    allowed_domains = ['https://www.fangstar.com/zufang']
    start_urls = ['https://www.fangstar.com/zufang']

    def parse(self, response):
        pass
