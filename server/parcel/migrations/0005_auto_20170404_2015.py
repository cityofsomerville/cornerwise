# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-05 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0004_parcel_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='map_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
