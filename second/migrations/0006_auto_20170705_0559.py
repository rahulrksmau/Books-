# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 05:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0005_auto_20170704_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 5, 5, 59, 29, 708756, tzinfo=utc)),
        ),
    ]