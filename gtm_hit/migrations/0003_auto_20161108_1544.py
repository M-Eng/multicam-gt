# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtm_hit', '0002_auto_20161108_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='workerID',
            field=models.TextField(default='', max_length=40),
        ),
    ]