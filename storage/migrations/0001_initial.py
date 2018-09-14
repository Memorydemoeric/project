# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-14 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StorageHalfFinished',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('half_id', models.CharField(max_length=64, unique=True)),
                ('half_type', models.CharField(max_length=256)),
                ('half_count', models.IntegerField(default=0)),
                ('half_cost_unit_price', models.FloatField(default=0.0)),
                ('half_sell_unit_price', models.FloatField(default=0.0)),
                ('half_sell_price', models.FloatField(default=0.0)),
                ('half_heading_code', models.CharField(default='-', max_length=64)),
                ('is_delete', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'syc_stor_half_finished',
            },
        ),
        migrations.CreateModel(
            name='StorageProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_id', models.CharField(max_length=64, unique=True)),
                ('pro_type', models.CharField(max_length=256)),
                ('pro_count', models.IntegerField(default=0)),
                ('pro_cost_unit_price', models.FloatField(default=0)),
                ('pro_sell_unit_price', models.FloatField(default=0)),
                ('pro_sell_price', models.FloatField(default=0.0)),
                ('pro_heading_code', models.CharField(default='-', max_length=64)),
                ('is_delete', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'syc_stor_product',
            },
        ),
    ]
