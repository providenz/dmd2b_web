# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160803_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='PatientID',
            field=models.CharField(max_length=50),
        ),
    ]
