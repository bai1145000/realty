# -*- coding: utf-8 -*-
import scrapy
from realty_spider.realty_spider.items import FangxingErshouItems
import time
from fangxing.models import FangxingErshouShangpu

class FangxingSpider(scrapy.Spider):
    '''房星'''
    name = 'fangxing'
    allowed_domains = ['fangstar.com']
    queryset = FangxingErshouShangpu.objects.all()

    def __init__(self,method=None,*args, **kwargs):
        super(FangxingSpider,self).__init__(*args, **kwargs)
        self.method = method

    def start_requests(self):
        # for i in 
        urls = 'https://www.fangstar.com/ershoufang/'
        for i in ['chenggongqu','ans','jnq','smx','ylx','fmx','guanduqu','wuhuaqu','lanlongqu','xishanqu',]:
            url = urls + i
            yield scrapy.Request(
                    url=url,
                    callback= self.parse
                )
    def parse(self,response):
        '''二级地区'''
        dd_list = response.xpath('//*[@class="cl trading-area"]/dd')
        for dd in dd_list[1:]:
            url = dd.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url,callback= self.list) #二级地区回调

    def list(self, response):
        '''列表页'''
        dd_list = response.xpath('//*[@class="cl trading-area"]/dd')
        for dd in dd_list:
            url = dd.xpath('./a/@href').extract_first()
            yield scrapy.Request(
                    url=url,
                    callback= self.parse
                )
       
        for i in response.xpath('//*[@class = "house-list fl"]/li'):
            items = {}
            items['url'] = i.xpath('./a/@href').extract_first()
            items['community'] = i.xpath('./div/em[1]/a/text()').extract_first() 
            address = i.xpath('./div/em[2]/span/a/text()').extract()
            items['address'] = address[0] + '-'+ address[1] 
            total_price =  i.xpath('./div/div/h3/text()').extract_first()
            items['total_price'] =  total_price + '万' if total_price else None
            publish_time = i.xpath('./div/em[3]/span/text()').extract_first()
            items['publish_time'] = publish_time.split('发')[0] if publish_time else None
            items['house_type'] = i.xpath('./div/em[1]/span[2]/text()').extract_first() 
            items['surrounding_school'] = i.xpath('./div/div[1]/span/text()').extract_first()
            # yield items
            yield scrapy.Request(
                response.urljoin(items['url']), callback= self.parse_details, meta={'items':items}
                )
        #下一页
        next_url = response.xpath('//*[@class = "tcdPageCode"]/a[last()]/@href').extract_first()
        if next_url:
            yield scrapy.Request(response.urljoin(next_url), callback= self.list)


    def parse_details(self,response):
        '''详情页'''
        meta_items = response.meta.get('items') #meta
        item = FangxingErshouItems() #model
        meta_items['uuid'] = response.xpath('//*[@class="info-row"][4]/span[2]/text()').extract_first()
        fx_fields = { #存储extra_items的引用
            'unit_price':'房屋单价','house_area':'建筑面积', 'content_two_five':'满二满五',
            'house_direction':'房屋朝向','house_usage':'房屋用途','double_certificate_situation':'双证情况',
            'stair_type':'楼梯类型','property_year':'产权年限','is_unique':'是否唯一','ladder_household_ratio':'梯  户  数',
            'floor':'所在楼层','house_renovation_type':'装修程度','building_year':'建造年代','building_type':'房屋类型',
            } 
        information = response.xpath('//*[@class="house-basic-info"]')
        for i in information.xpath('./li'):   #小区详情
            label = i.xpath('./span[@class="label"]/text()').extract_first()
            value = i.xpath('./span[2]/text()').extract_first()
            key = FangxingSpider.get_key(fx_fields,label) #根据值获取key
            if  len(key) != 0:
                meta_items.update( {key[0]:value})   #动态设置值

        item.update(meta_items)
        del meta_items #释放资源
        yield  item

    @staticmethod
    def get_key(dct, value):
        return list(filter(lambda k:dct[k] == value, dct))
