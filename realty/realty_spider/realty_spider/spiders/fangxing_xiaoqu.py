# -*- coding: utf-8 -*-
import scrapy
from realty_spider.realty_spider.items import FangxingXiaoquItems

class FangxingXiaoquSpider(scrapy.Spider):
    name = 'fangxing_xiaoqu'
    allowed_domains = ['www.fangstar.com']
    # start_urls = ['https://www.fangstar.com/xiaoqu/']

    def start_requests(self):
        # for i in 
        urls = 'https://www.fangstar.com/xiaoqu/'
        for i in ['guanduqu','wuhuaqu','lanlongqu','chenggongqu','ans','jnq','smx','ylx','fnx','xishangqu',]:
            url = urls + i
            yield scrapy.Request(
                    url=url,
                    callback= self.parse
                )


    def parse(self, response):
        '''小区列表页'''
        for i in response.xpath('//*[@class = "house-list fl"]/li'):
            items = {}
            items['url'] = i.xpath('./a/@href').extract_first()
            items['community'] = i.xpath('./div/h3/a/text()').extract_first()
            items['unit_price'] = i.xpath('./div/div[@class="school-price"]/h3/text()').extract_first()
            items['address'] = i.xpath('.div/em/span[@class="padging-l35 omit"]/text()').extract_first()
            building_year = i.xpath('./div/em[1]/span/text()').extract_first()
            items['building_year'] = building_year.split('：')[1][:-1] if '暂' in building_year else None
            items['surrounding_school'] = i.xpath('./div/div[@class="list-label-box"]/span/text()').extract_first()
            # yield items
            yield scrapy.Request(
                response.urljoin(items['url']), callback = self.parse_details, meta={'items': items}
                )
        
        next_url = response.xpath('//*[@class = "tcdPageCode"]/a[last()]/@href').extract_first() #执行回调
        if next_url:
            yield scrapy.Request(response.urljoin(next_url), callback= self.parse)

    def parse_details(self,response):
        '''详情页'''
        meta_items = response.meta.get('items')
        item = FangxingXiaoquItems()
        details = response.xpath('//*[@class="pz-row"]')  #基本信息
        item['volumetric_flow_rate'] = details.xpath('./div[@class="lf"]/dl[1]/dd/text()').extract_first()
        item['green_rate'] = details.xpath('./div[@class="lf"]/dl[2]/dd/text()').extract_first() #绿化率
        item['property_type'] = details.xpath('./div[@class="lf"]/dl[4]/dd/text()').extract_first() 
        item['household_num'] = details.xpath('./div[@class="rt"]/dl[1]/dd/text()').extract_first()
        item['park_num'] = details.xpath('./div[@class="rt"]/dl[2]/dd/text()').extract_first()
        item['property_price'] = details.xpath('./div[@class="rt"]/dl[3]/dd/text()').extract_first()
        item['property_company'] = details.xpath('./div[@class="rt"]/dl[4]/dd/text()').extract_first()
        item['developer'] = response.xpath('//dl[@class="overflow"]/dd/text()').extract_first()

        rent_num = response.xpath('//*[@id="chuZuFangYuan"]/h2/a/text()')
        item['rent_num'] = rent_num.extract_first().split('(')[1].split('套')[0] if rent_num else None #出租房源
        sale_num = response.xpath('//*[@id="zaiShouFangYuan"]/h2/a/text()').extract_first()
        item['sale_num'] = sale_num.split('(')[1].split('套')[0] if sale_num else None #在售房源

        xq_fields = {   #存储extra_items的引用
           'community_detail':'小区详情','park_price':'停车费','building_num':'楼栋总数','water_price':'自来水费',
            'lift_price':'电梯使用费','decoration_margin':'装修保证金','maintenance_fund':'维修基金','health_price':'卫生费用',
            'gas_price':'gas_price','junk_cleaning_price':'垃圾清理费','wastewater_price':'污水处理费','construction_waste_price':'建筑垃圾清理费',
            'electricity_price':'电费','bicycle_parking_price':'非机动车停车费','other_property_price':'其他物业费','property_phone':'物业办公电话','deal_unit_mom':'',
            'property_address':'物业办公地址','street_office':'所辖街道办','police_station':'所辖派出所','listing_unit_price':'挂牌均价','listing_unit_mom':'挂牌均价的月环比',
            'deal_unit_price':'成交均价','deal_unit_mom':'成交均价的月环比'} 

        for i in response.xpath('//div[@class="info clearfix"]/ul/li'):
            key = i.xpath('./text()').extract_first().split('：')[0]
            value = i.xpath('./span/text()').extract_first()
            key = FangxingXiaoquSpider.get_key(xq_fields,key) #根据值获取key
            if  len(key) != 0:
                meta_items.update( {key[0]:value})   #动态设置值

        average_price = response.xpath('//*[@class="clearfix"]') #均价
        listing_unit_price = average_price.xpath('./li[1]//div/h3/i/text()').extract_first() #挂牌均价
        item['listing_unit_price'] = listing_unit_price + '元/m²' if listing_unit_price else None
        deal_unit_price = average_price.xpath('./li[2]//div/h3/i/text()').extract_first() #成交均价
        item['deal_unit_price'] = deal_unit_price + '元/m²' if deal_unit_price else None

        item.update(meta_items)
        del meta_items #释放资源
        yield  item

    @staticmethod
    def get_key(dct, value):
        return list(filter(lambda k:dct[k] == value, dct))
