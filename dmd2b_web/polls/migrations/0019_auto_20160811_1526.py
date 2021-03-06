# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20160811_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='Age_Days',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='PatientBirthDate',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='PatientID',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='PatientName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='PatientReportedAge',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='PatientSex',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='seriesdetails',
            name='Modality',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='seriesdetails',
            name='SeriesDescription',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='seriesdetails',
            name='SeriesID',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studydetails',
            name='StudyDate',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='studydetails',
            name='StudyDescription',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studydetails',
            name='StudyID',
            field=models.CharField(max_length=50),
        ),
    ]
