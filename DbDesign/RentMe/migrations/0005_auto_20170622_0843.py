# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 00:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentMe', '0004_auto_20170622_0829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model_info',
            old_name='car_flue_type',
            new_name='car_fuel_type',
        ),
    ]
