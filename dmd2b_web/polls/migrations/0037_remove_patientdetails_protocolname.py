# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-12 15:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0036_remove_patientdetails_primaryslicedirection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdetails',
            name='ProtocolName',
        ),
    ]
