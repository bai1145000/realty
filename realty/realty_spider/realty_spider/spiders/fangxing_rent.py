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
    queryset = FangxingRent.objects.all()
    
    def __init__(self,method=None,*args, **kwargs):
        super(FangxingRentSpider,self).__init__(*args, **kwargs)
        self.method = method

    rules = (
        Rule(LinkExtractor(allow=r'/zufang/[a-z]\D+$'), follow=True),
        Rule(LinkExtractor(allow=r'/zufang/[a-z]\D+$'), callback='parse_item', follow=True,),#请求list
        Rule(LinkExtractor(allow=r'/zufang/pg\d+$'), follow=True), #翻页请求
    )
    def parse_start_url(self, response):
        return super().parse_start_url( response)
    def parse_item(self, response):
        '''列表页'''
        for i in response.xpath('//*[@class = "house-list fl"]/li'):
            item = {}
            item['url'] = i.xpath('./a/@href').extract_first()
            item['community'] = i.xpath('./div/em[1]/a/text()').extract_first() #出租房所在小区名字
            address = i.xpath('./div/em[2]/span/a/text()').extract()
            item['address'] = address[0] + '-'+ address[1] if len(address)>=2 else address[0]
            total_price =  i.xpath('./div/div/h3/text()').extract_first() + i.xpath('./div/div/h3/span/text()').extract_first()
            item['rent_price'] =  total_price
            publish_time = i.xpath('./div/em[3]/span/text()').extract_first()
            item['publish_time'] = publish_time.split('发')[0] if publish_time else None
            item['house_type'] = i.xpath('./div/em[1]/span[2]/text()').extract_first() 
            # print(i)
            yield scrapy.Request(
                url= item['url'],meta={'items':item},callback=self.parse_details
            )
        
    def parse_details(self, response):
        '''详情页'''
        meta_items = response.meta.get('items')
        item = FangxingZufangItems()
        fx_fields={
            '房屋用途':'house_usage','装修程度':'house_renovation_type','房屋类型':'house_type',
            '楼梯类型':'stair_type','梯  户 数':'ladder_household_ratio','入       住':'check_in_time',
            '洗衣机':'is_washing','热水器':'is_fridge','电视':'is_tv','冰箱':'is_fridge','沙发':'is_sofa',
            '宽带':'is_net','天然气':'is_natural_gas','微波炉':'is_microwave',
            '热水器':'is_hot_water','衣柜':'is_closet','床':'is_bed'
            }
        for i in response.xpath('//ul[@class="house-basic-info"]/li'): #房屋基本信息
            label = i.xpath('./span[@class="label"]/text()').extract_first()
            value = i.xpath('./span[2]/text()').extract_first()
            key = fx_fields.get(label)
            meta_items.update({key:value})

        #存在的家电设施
        appliances = {fx_fields.get(k):1 for k in response.xpath('//div[@class="content"]/div/div/img/@alt').extract()}
        if appliances:
            meta_items.update(appliances)
        
        #基本资料
        zufang_path = response.xpath('//div[@class="wrap"]')
        item['uuid'] = zufang_path.xpath('./div[@class="info-wrap"]/div[4]/span[@class="value"]/text()').extract_first()
        item['house_area'] = zufang_path.xpath('./div[@class="important"]/span[2]/text()').extract_first()
        item['house_direction'] = zufang_path.xpath('./div[@class="important"]/span[3]/text()').extract_first()
        item['floor'] = zufang_path.xpath('./div[@class="info-wrap"]/div[3]/span[@class="value"]/text()').extract_first()
        item['rent_type'] = response.xpath('//div[@class="price-wrap"]/span[@class="other-info"]/text()').extract_first()
        
        item.update(meta_items)
        del fx_fields
        del meta_items
        yield item