# -*- coding: utf-8 -*-
import scrapy
from realty_spider.realty_spider.items import ZhugexiaoquItems

class ZhugeXiaoquSpider(scrapy.Spider):
    name = 'zhuge_xiaoqu'
    allowed_domains = ['zhuge.com']
    start_urls = ['http://km.xiaoqu.zhuge.com/']
    '''id	url	community	address	unit_price	property_type	building_type	unit_price_mom	
    building_year	property_year	building_num	household_num	floor_area	building_area	
    volumetric_flow_rate	green_ratio	developer	property_company	property_price	property_office_address	
    proper_phone	sale_num	rent_num	highest_price	lowest_price	surrounding_mediation	water_type	
    heating_type	electricity_type	communication_equipment	lift_service	crawl_time'''
    def parse(self, response):
        '''列表页'''
        for i in response.xpath('//*[@id="listTableBox"]/li'):
            item = ZhugexiaoquItems()
            item['url'] = i.xpath('./a/@href').extract_first()
            item['community'] = i.xpath('./div/p[@class="house-name"]/a/text()').extract_first()
            item['address'] = i.xpath('/div/p[@class="house-adr f14"]/text()').extract_first()
            item['unit_price'] = i.xpath('./div[@class="list-price"]/p[1]/span').extract_first() + '元/m*m'
            build_type =  i.xpath('./div/p[@class="house-build-time f14"]/text()').extract_first()
            item['property_type'] = build_type.split('/')[0] if build_type else None
            item['building_year'] = build_type.split('/')[1] if len(build_type)>1 else None
            item['unit_price_mom'] = i.xpath('./div[2]/p[@class="price-compare"]/span[2]').extract_first() #均价环比
            yield item

        next_url = response.xpath('//*[@class="laypage-main"]/a[@class="laypage-next"]/@href').extract_first()
        if next_url:
            yield scrapy.Request(response.urljoin(next_url), callback= self.parse)




