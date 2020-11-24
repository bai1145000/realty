# -*- coding: utf-8 -*-
import sys ,os
from fangxing.models import FangxingErshouShangpu, FangxingXiaoqu


class FangxingErshouPipeline(object):
    '''房星二手房'''
    def process_item(self, item, spider):

        if spider.name == 'fangxing':
            if FangxingErshouShangpu.objects.filter(url =item['url']):  #过滤重复保存
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
            # FangxingErshouShangpu.objects.create(**item)
            item.save()
        return item

class FangxingXiaoquPipeline(object):
    '''房星小区房'''
    def process_item(self, item, spider):
        if spider.name == 'fangxing_xiaoqu':
            if FangxingXiaoqu.objects.filter(url =item['url']):  #过滤重复保存
                return item
            #去除空格换行
            for i in ['community','property_type','property_price','volumetric_flow_rate','green_rate','surrounding_school','bicycle_parking_price']:
                if item.get(i):
                    item[i] = item[i ].replace(" ","").replace("\r","").replace("\n","") 

            type_int = [k for k in item.fields if 'num' in k ] + ['building_year']  #需要转化为数字的数值
            for i in type_int:
                if item.get(i) and item.get(i) != '暂':
                    item[i] =  0 if item[i] == '--' else int(item[i])
                elif item.get(i) == '暂':
                    item[i] = None
            
            item['volumetric_flow_rate'] = 0 if item['volumetric_flow_rate'] == '--' else float(item['volumetric_flow_rate'])
            item.save()
        return item


class ZhugeXiaoquPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'zhuge_xiaoqu':

            return item

