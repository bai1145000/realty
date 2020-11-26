# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from fangxing.models import FangxingErshouShangpu, FangxingXiaoqu ,FangxingRent, FangxingXuexiao
from zhuge.models import  ZhugeXiaoqu
   

class FangxingErshouItems(DjangoItem):
    '''房星二手商铺'''
    django_model = FangxingErshouShangpu

class FangxingXiaoquItems(DjangoItem):
    '''房星小区'''
    django_model = FangxingXiaoqu

class FangxingZufangItems(DjangoItem):
    '''房星租房'''
    django_model = FangxingRent

class FangxingSchoolItems(DjangoItem):
    '''房星学校'''
    django_model = FangxingXuexiao



class ZhugexiaoquItems(DjangoItem):
    '''诸葛小区'''
    django_model = ZhugeXiaoqu
