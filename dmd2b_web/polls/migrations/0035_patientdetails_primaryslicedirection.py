# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-08 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0034_patientdetails_protocolname'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdetails',
            name='PrimarySliceDirection',
            field=models.CharField(default=5489451, max_length=100),
            preserve_default=False,
        ),
    ]
