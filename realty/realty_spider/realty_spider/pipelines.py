# -*- coding: utf-8 -*-
import sys ,os
from fangxing.models import FangxingErshouShangpu, FangxingXiaoqu
import re

class FangxingErshouPipeline(object):
    '''房星二手房'''
    def process_item(self, item, spider):

        if spider.name == 'fangxing' :
            if spider.queryset.filter(url =item['url']):  #过滤重复保存
                return item
            floor = item.get('floor')
            if floor:  #对数据分支处理
                floor = floor.split('/') if floor != '--' or bool(floor) else ['-','-']
                item['floor'] = floor[0]
                item['total_floor'] = int(str(floor[1])[:-1])
            for i in ['community','publish_time','surrounding_school']:
                if item.get(i):
                    item[i] = item[i ].replace(" ","").replace("\r","").replace("\n","") 
            item['is_unique'] = 1 if item.get('is_unique') =='是' else 0
            item.save()
        return item

class FangxingXiaoquPipeline(object):
    '''房星小区房'''
    def process_item(self, item, spider):
        if spider.name == 'fangxing_xiaoqu':
            if spider.queryset.filter(url =item['url']):  #过滤重复保存
                return item
            #去除空格换行
            for i in ['community','property_type','property_price','volumetric_flow_rate','green_rate','surrounding_school','bicycle_parking_price']:
                if item.get(i):
                    item[i] = item[i ].replace(" ","").replace("\r","").replace("\n","").replace("]","") 

            type_int = [k for k in item.fields if 'num' in k ] + ['building_year']  #需要转化为数字的数值
            for i in type_int:
                if item.get(i) and item.get(i) != '暂':
                    item[i] =  0 if item[i] == '--' else int(item[i])
                elif item.get(i) == '暂':
                    item[i] = None
            
            item['volumetric_flow_rate'] = 0 if item['volumetric_flow_rate'] == '--' else float(item['volumetric_flow_rate'])
            item.save()
        return item

class FangxingRentPipeline(object):
    '''房星二手房'''
    def process_item(self, item, spider):
        if spider.name == 'fangxing_rent':
            if spider.queryset.filter(url =item['url'] ):
                return item
            item.save()
        return item


class FangxingSchoolPipeline(object):
    '''房星学校'''
    def process_item(self, item, spider):
        if spider.name ==  'fangxing_school':
            if spider.queryset.filter(url =item['url'] ):
                return item
            for i in ['school_nature']:
                if item.get(i):
                    item[i] = item[i ].replace(" ","").replace("\r","").replace("\n","")
            item.save()
        return item

class ZhugeXiaoquPipeline(object):
    '''诸葛小区'''
    def process_item(self, item, spider):
        if spider.name == 'zhuge_xiaoqu':
            if spider.queryset.filter(url =item['url'] ):
                return item
            for i in ['building_year','property_type','unit_price_mom','address']:
                if item.get(i):
                    item[i] = item[i ].replace(" ","").replace("\r","").replace("\n","")
            item['address'] =  item['address'][1:] if  item['address'] else None
            type_a_year =  item['property_type'].split('/') if len(item['property_type'])>4 else item['property_type']
            item['unit_price'] = None if '暂' in item['unit_price'] else item['unit_price']
            item['property_type'] = type_a_year[0]  if len(type_a_year) == 1 else None
            building_year = re.search('\d+',type_a_year[1]).group(0) if len(type_a_year)>=2 and isinstance(type_a_year,list) else None
            item['building_year'] = int(building_year) if building_year else None
            item['unit_price_mom'] = item['unit_price_mom'].replace(" ","")[:-1]  if  item['unit_price_mom'] else None
            item.save()
        return item