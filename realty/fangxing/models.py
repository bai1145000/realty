from django.db import models

# Create your models here.
class FangxingErshouShangpu(models.Model):
    '''房星二手商铺'''
    url = models.CharField(max_length=64, blank=True, null=True,verbose_name= '数据来源')
    uuid = models.CharField(max_length=30, blank=True, null=True,verbose_name= '房源编号')
    community = models.CharField(max_length=32, blank=True, null=True ,verbose_name='小区名称')
    address = models.CharField(max_length=30, blank=True, null=True,verbose_name='所在区域')
    total_price = models.CharField(max_length=8, blank=True, null=True,verbose_name= '总价格')
    publish_time = models.DateField(blank=True, null=True,verbose_name= '公布时间')
    house_type = models.CharField(max_length=64, blank=True, null=True ,verbose_name='房屋户型')
    unit_price = models.CharField(max_length=8, blank=True, null=True,verbose_name= '房屋单价')
    house_renovation_type = models.CharField(max_length=64, blank=True, null=True,verbose_name= '装修程度')
    house_area = models.CharField(max_length=64, blank=True, null=True,verbose_name= '建筑面积')
    house_direction = models.CharField(max_length=64, blank=True, null=True ,verbose_name='房屋朝向')
    building_type = models.CharField(max_length=64, blank=True, null=True ,verbose_name='房屋类型')
    house_usage = models.CharField(max_length=64, blank=True, null=True ,verbose_name='房屋用途') 
    double_certificate_situation = models.CharField(max_length=64, blank=True, null=True,verbose_name= '双证情况')
    total_floor = models.IntegerField(blank=True, null=True,verbose_name= '总楼层')
    floor = models.CharField(max_length=8, blank=True, null=True ,verbose_name='所在楼层')
    building_year = models.CharField(max_length=64, blank=True, null=True,verbose_name='建造年代')
    content_two_five = models.CharField(max_length=64, blank=True, null=True,verbose_name= '满二满五')
    stair_type = models.CharField(max_length=64, blank=True, null=True ,verbose_name='楼梯类型')
    property_year = models.CharField(max_length=64, blank=True, null=True ,verbose_name='产权年限')
    is_unique = models.IntegerField(blank=True, null=True ,verbose_name='是否唯一')
    ladder_household_ratio = models.CharField(max_length=64, blank=True, null=True ,verbose_name='梯户数')
    surrounding_school = models.CharField(max_length=255, blank=True, null=True ,verbose_name='房屋周围的学校')
    crawl_time = models.DateTimeField(blank=True, null=True,auto_now=True,verbose_name='爬取时间')

    class Meta:
        managed = False
        db_table = 'fangxing_ershou'

class FangxingRelate(models.Model):
    school = models.CharField(max_length=64)
    community = models.CharField(max_length=128, blank=True, null=True)
    price = models.CharField(max_length=32, blank=True, null=True)
    build_year = models.CharField(max_length=32, blank=True, null=True)
    distance = models.CharField(max_length=32, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fangxing_relate'

class FangxingRent(models.Model):
    '''房星租房'''
    url = models.CharField(max_length=64, blank=True, null=True)
    uuid = models.CharField(max_length=30, blank=True, null=True ,verbose_name='房源编号')
    rent_price = models.CharField(max_length=64, blank=True, null=True)
    rent_type = models.CharField(max_length=64, blank=True, null=True)
    house_type = models.CharField(max_length=64, blank=True, null=True)
    house_area = models.CharField(max_length=8, blank=True, null=True)
    house_direction = models.CharField(max_length=64, blank=True, null=True)
    community = models.CharField(max_length=64, blank=True, null=True,verbose_name= '小区名称')
    address = models.CharField(max_length=64, blank=True, null=True ,verbose_name='所在区域')
    total_floor = models.IntegerField(blank=True, null=True)
    floor = models.CharField(max_length=64, blank=True, null=True)
    publish_time = models.DateField(blank=True, null=True)
    house_usage = models.CharField(max_length=64, blank=True, null=True)
    house_renovation_type = models.CharField(max_length=64, blank=True, null=True)
    stair_type = models.CharField(max_length=64, blank=True, null=True)
    ladder_household_ratio = models.CharField(max_length=64, blank=True, null=True)
    check_in_time = models.CharField(max_length=64, blank=True, null=True)
    is_fridge = models.IntegerField(blank=True, null=True)
    is_washing = models.IntegerField(blank=True, null=True)
    is_hot_water = models.IntegerField(blank=True, null=True)
    is_tv = models.IntegerField(blank=True, null=True)
    is_microwave = models.IntegerField(blank=True, null=True)
    is_bed = models.IntegerField(blank=True, null=True)
    is_closet = models.IntegerField(blank=True, null=True)
    is_sofa = models.IntegerField(blank=True, null=True)
    is_net = models.IntegerField(blank=True, null=True)
    is_natural_gas = models.IntegerField(blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        managed = False
        db_table = 'fangxing_rent'

class FangxingXiaoqu(models.Model):
    '''房星小区'''
    url = models.CharField(max_length=64, blank=True, null=True, verbose_name='数据来源地址')
    community = models.CharField(max_length=64, blank=True, null=True ) 
    unit_price = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    volumetric_flow_rate = models.FloatField(blank=True, null=True)
    household_num = models.IntegerField(blank=True, null=True)
    green_rate = models.CharField(max_length=164, blank=True, null=True)
    park_num = models.IntegerField(blank=True, null=True)
    building_year = models.IntegerField(blank=True, null=True)
    property_price = models.CharField(max_length=12, blank=True, null=True)
    property_type = models.CharField(max_length=64, blank=True, null=True)
    property_company = models.CharField(max_length=255, blank=True, null=True)
    developer = models.CharField(max_length=255, blank=True, null=True)
    surrounding_school = models.CharField(max_length=30, blank=True, null=True)
    rent_num = models.IntegerField(blank=True, null=True)
    sale_num = models.IntegerField(blank=True, null=True)
    community_detail = models.CharField(max_length=255, blank=True, null=True)
    park_price = models.CharField(max_length=64, blank=True, null=True)
    building_num = models.IntegerField(blank=True, null=True)
    water_price = models.CharField(max_length=64, blank=True, null=True)
    lift_price = models.CharField(max_length=64, blank=True, null=True)
    decoration_margin = models.CharField(max_length=64, blank=True, null=True)
    maintenance_fund = models.CharField(max_length=64, blank=True, null=True)
    health_price = models.CharField(max_length=64, blank=True, null=True)
    electricity_price = models.CharField(max_length=64, blank=True, null=True)
    gas_price = models.CharField(max_length=64, blank=True, null=True)
    junk_cleaning_price = models.CharField(max_length=64, blank=True, null=True)
    wastewater_price = models.CharField(max_length=64, blank=True, null=True)
    construction_waste_price = models.CharField(max_length=64, blank=True, null=True)
    bicycle_parking_price = models.CharField(max_length=64, blank=True, null=True)
    other_property_price = models.CharField(max_length=64, blank=True, null=True)
    property_phone = models.CharField(max_length=64,blank=True, null=True)
    property_address = models.CharField(max_length=32, blank=True, null=True)
    street_office = models.CharField(max_length=12, blank=True, null=True)
    police_station = models.CharField(max_length=64, blank=True, null=True)
    listing_unit_price = models.CharField(max_length=64, blank=True, null=True)
    listing_unit_mom = models.CharField(max_length=64, blank=True, null=True)
    deal_unit_price = models.CharField(max_length=64, blank=True, null=True)
    deal_unit_mom = models.CharField(max_length=64, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        managed = False
        db_table = 'fangxing_xiaoqu'


class FangxingXuexiao(models.Model):
    '''房星学校'''
    school = models.CharField(max_length=64, blank=True, null=True)
    region = models.CharField(max_length=64, blank=True, null=True)
    school_type = models.CharField(max_length=64, blank=True, null=True)
    school_nature = models.CharField(max_length=44, blank=True, null=True)
    location = models.CharField(max_length=64, blank=True, null=True)
    pair_school = models.CharField(max_length=64, blank=True, null=True)
    uuid = models.CharField(max_length=64, blank=True, null=True)
    url = models.CharField(max_length=64, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fangxing_xuexiao'