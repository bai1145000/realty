# -*- coding: utf-8 -*-
import sys ,os
from fangxing.models import FangxingErshouShangpu, FangxingXiaoqu,FangxingRent
import re

class StringPipeline(object):
    '''对字符清洗'''
    def __init__(self,*args, **kwargs):
        self.spider_dict = {
            'fangxing_xiaoqu':['community','property_type','property_price','volumetric_flow_rate',
                    'green_rate','surrounding_school','bicycle_parking_price','community_detail'],
            'fangxing':['community','publish_time','surrounding_school'],
            'fangxing_school':['school_nature'],
            'zhuge_xiaoqu':['building_year','property_type','unit_price_mom','address'],
        }
    def process_item(self, item, spider):
        #去除空格换行
        str_list = self.spider_dict.get(spider.name,[])
        for i in str_list:
            if item.get(i):
                item[i] = item[i ].replace(" ","").replace("\r","").replace("\n","").replace("]","")
        return item

class FangxingErshouPipeline(object):
    '''房星二手房'''
    def process_item(self, item, spider):
        if spider.name == 'fangxing':
            method = spider.method
            floor = item.get('floor')
            if floor:  #对数据分支处理 楼层
                floor = floor.split('/') if floor != '--' or bool(floor) else ['-','-']
                item['floor'] = floor[0]
                item['total_floor'] = int(str(floor[1])[:-1])
            item['is_unique'] = 1 if item.get('is_unique') =='是' else 0
        return item

class FangxingXiaoquPipeline(object):
    '''房星小区房'''
    def process_item(self, item, spider):
        if spider.name == 'fangxing_xiaoqu':
        
            type_int = [k for k in item.fields if 'num' in k ] + ['building_year']  #需要转化为数字的数值
            for i in type_int:
                if item.get(i) and item.get(i) != '暂':
                    item[i] =  None if item[i] == '--' else int(item[i])
                elif item.get(i) == '暂':
                    item[i] = None
            item['volumetric_flow_rate'] = 0 if item['volumetric_flow_rate'] == '--' else float(item['volumetric_flow_rate'])
         
        return item

class FangxingRentPipeline(object):
    '''房星租房'''
    def process_item(self, item, spider):
        if spider.name == 'fangxing_rent':
            floor = item.get('floor')
            if floor:  #对数据分支处理 楼层
                floor = floor.split('/') if floor != '--' or bool(floor) else ['-','-']
                item['floor'] = floor[0]
                item['total_floor'] = int(str(floor[1])[:-1])
        return item


class FangxingSchoolPipeline(object):
    '''房星学校'''
    def process_item(self, item, spider):
        if spider.name ==  'fangxing_school':
            pass
        return item

class ZhugeXiaoquPipeline(object):
    '''诸葛小区'''
    def process_item(self, item, spider):
        if spider.name == 'zhuge_xiaoqu':
            item['address'] =  item['address'][1:] if  item['address'] else None
            type_a_year =  item['property_type'].split('/') if len(item['property_type'])>4 else item['property_type']
            item['unit_price'] = None if '暂' in item['unit_price'] else item['unit_price']
            item['property_type'] = type_a_year[0]  if len(type_a_year) == 1 else None
            building_year = re.search('\d+',type_a_year[1]).group(0) if len(type_a_year)>=2 and isinstance(type_a_year,list) else None
            item['building_year'] = int(building_year) if building_year else None
            item['unit_price_mom'] = item['unit_price_mom'].replace(" ","")[:-1]  if  item['unit_price_mom'] else None
        return item

class SavePipine(object):
    '''更新和保存'''
    def __init__(self,method=None,*args, **kwargs):
        self.method = method

    def process_item(self, item, spider):
        obj = spider.queryset.filter(url=item['url'])
        if obj and  spider.method == 'update':
            obj.update(**item)
        else:
            item.save()
        return item
