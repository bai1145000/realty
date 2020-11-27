# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from realty_spider.realty_spider.items import ZhugexiaoquItems
from scrapy.spiders import CrawlSpider, Rule
from zhuge.models import  ZhugeXiaoqu

class ZhugeXiaoquSpider(CrawlSpider):
    name = 'zhuge_xiaoqu'
    allowed_domains = ['zhuge.com']
    start_urls = ['https://km.xiaoqu.zhuge.com/']
    queryset = ZhugeXiaoqu.objects.all()
    rules = (
        Rule(LinkExtractor(allow=r'/page\d+/$'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/[a-z]$'), callback='parse_item',follow=True),
    ) 
    custom_settings = {
    'ITEM_PIPELINES':{'realty_spider.realty_spider.pipelines.StringPipeline':300,  #str清洗
        'realty_spider.realty_spider.pipelines.ZhugeXiaoquPipeline': 300,
        'realty_spider.realty_spider.pipelines.SavePipine':300  #保存
        },
        'DEFAULT_REQUEST_HEADERS':{
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)',
            "Cookie": "_WEB_newtoken=; _WEB_USER_ID=1606183236231933; _WEB_token=yuL8hEedSZP5G4tb--fLmQYY0NLs_k2DN0t8C35yoEV-ywrILxBv-colR3hp0Xka3lsM7J0j2WP4XxM0ilGPYQ%3D%3D; _WEB_city_code=km; _WEB_city_name=%E6%98%86%E6%98%8E; _WEB_qtoken=; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22175f7fb417d302-037fbf46c632d6-333376b-1327104-175f7fb417e6a%22%2C%22%24device_id%22%3A%22175f7fb417d302-037fbf46c632d6-333376b-1327104-175f7fb417e6a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; Hm_lvt_8d409b931bc5e2ac53a0cea966f06d99=1606183240; _WEB_page_type=web; _WEB_cityid=18; _WEB_ip_cityCode=km; _WEB_ip_cityName=%E6%98%86%E6%98%8E; acw_tc=2760824116062054458431246e7ae1e3839a44f423110a665955721cc5606e; acw_sc__v2=5fbcc211112aabb62e86666beb7182596fe87516; _ga=GA1.2.1878803091.1606205974; _gid=GA1.2.477647664.1606205974; Hm_lpvt_8d409b931bc5e2ac53a0cea966f06d99=1606205994",
            "Referer":'http://km.zhuge.com/',
            'Host': 'km.xiaoqu.zhuge.com',
            'Connection': 'keep-alive',
            'Content-Encoding':' gzip'
        },
        'FEED_EXPORT_ENCODING' :'ascii'
    }

    def parse_item(self, response): 
        '''列表页'''
        for i in response.xpath('//*[@id="listTableBox"]/li'):
            item = ZhugexiaoquItems()
            item['url'] = i.xpath('./a/@href').get()
            item['community'] = i.xpath('./div/p[@class="house-name"]/a/text()').get()
            address =  i.xpath('./div/p[@class="house-adr f14"]/text()').extract()
            item['address'] = address[1] if len(address)>= 2 else address[0]
            item['unit_price'] = i.xpath('./div[@class="list-price"]/p[1]/span/text()').get() + '元/m*m'
            build_type =  i.xpath('./div/p[@class="house-build-time f14"]/text()').get()
            item['property_type'] = build_type
            item['unit_price_mom'] = i.xpath('./div[2]/p[@class="price-compare"]/span[2]/text()').get() #均价环比
            yield item

