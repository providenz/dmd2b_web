# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20160809_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='PatientBirthDate',
            field=models.DateTimeField(verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='studydetails',
            name='StudyDate',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
