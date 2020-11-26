# Generated by Django 3.0.7 on 2020-11-24 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZhugeXiaoqu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('community', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('unit_price', models.CharField(blank=True, max_length=20, null=True)),
                ('property_type', models.CharField(blank=True, max_length=20, null=True)),
                ('building_type', models.CharField(blank=True, max_length=20, null=True)),
                ('unit_price_mom', models.CharField(blank=True, max_length=20, null=True)),
                ('building_year', models.IntegerField(blank=True, null=True)),
                ('property_year', models.CharField(max_length=20)),
                ('building_num', models.IntegerField(blank=True, null=True)),
                ('household_num', models.IntegerField(blank=True, null=True)),
                ('floor_area', models.CharField(blank=True, max_length=20, null=True)),
                ('building_area', models.CharField(blank=True, max_length=20, null=True)),
                ('volumetric_flow_rate', models.FloatField(blank=True, null=True)),
                ('green_ratio', models.CharField(blank=True, max_length=20, null=True)),
                ('developer', models.CharField(blank=True, max_length=30, null=True)),
                ('property_company', models.CharField(blank=True, max_length=20, null=True)),
                ('property_price', models.CharField(blank=True, max_length=20, null=True)),
                ('property_office_address', models.CharField(blank=True, max_length=20, null=True)),
                ('proper_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('sale_num', models.IntegerField(blank=True, null=True)),
                ('rent_num', models.IntegerField(blank=True, null=True)),
                ('highest_price', models.CharField(blank=True, max_length=20, null=True)),
                ('lowest_price', models.CharField(blank=True, max_length=20, null=True)),
                ('surrounding_mediation', models.CharField(blank=True, max_length=20, null=True)),
                ('water_type', models.CharField(blank=True, max_length=20, null=True)),
                ('heating_type', models.CharField(blank=True, max_length=20, null=True)),
                ('electricity_type', models.CharField(blank=True, max_length=20, null=True)),
                ('communication_equipment', models.CharField(blank=True, max_length=20, null=True)),
                ('lift_service', models.CharField(blank=True, max_length=20, null=True)),
                ('crawl_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'zhuge_xiaoqu',
            },
        ),
    ]
