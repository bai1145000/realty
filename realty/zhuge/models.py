# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ZhugeXiaoqu(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    community = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    unit_price = models.CharField(max_length=20, blank=True, null=True)
    property_type = models.CharField(max_length=20, blank=True, null=True)
    building_type = models.CharField(max_length=20, blank=True, null=True)
    unit_price_mom = models.CharField(max_length=20, blank=True, null=True)
    building_year = models.IntegerField(blank=True, null=True)
    property_year = models.CharField(max_length=20)
    building_num = models.IntegerField(blank=True, null=True)
    household_num = models.IntegerField(blank=True, null=True)
    floor_area = models.CharField(max_length=20, blank=True, null=True)
    building_area = models.CharField(max_length=20, blank=True, null=True)
    volumetric_flow_rate = models.FloatField(blank=True, null=True)
    green_ratio = models.CharField(max_length=20, blank=True, null=True)
    developer = models.CharField(max_length=30, blank=True, null=True)
    property_company = models.CharField(max_length=20, blank=True, null=True)
    property_price = models.CharField(max_length=20, blank=True, null=True)
    property_office_address = models.CharField(max_length=20, blank=True, null=True)
    proper_phone = models.CharField(max_length=20, blank=True, null=True)
    sale_num = models.IntegerField(blank=True, null=True)
    rent_num = models.IntegerField(blank=True, null=True)
    highest_price = models.CharField(max_length=20, blank=True, null=True)
    lowest_price = models.CharField(max_length=20, blank=True, null=True)
    surrounding_mediation = models.CharField(max_length=20, blank=True, null=True)
    water_type = models.CharField(max_length=20, blank=True, null=True)
    heating_type = models.CharField(max_length=20, blank=True, null=True)
    electricity_type = models.CharField(max_length=20, blank=True, null=True)
    communication_equipment = models.CharField(max_length=20, blank=True, null=True)
    lift_service = models.CharField(max_length=20, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zhuge_xiaoqu'
