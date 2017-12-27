# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 12:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0008_auto_20170705_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='country',
            field=models.CharField(default='America', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 6, 12, 15, 29, 271216, tzinfo=utc)),
        ),
    ]