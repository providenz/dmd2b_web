# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_auto_20160830_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalheaderinfo',
            name='PatientID',
            field=models.CharField(max_length=100),
        ),
    ]
