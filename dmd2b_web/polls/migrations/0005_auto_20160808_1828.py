# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20160808_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studydetails',
            name='StudyDate',
            field=models.CharField(max_length=100),
        ),
    ]
