# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-02 02:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200502_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mezun',
            name='oncekiGirisIs',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 2, 41, 3, 970566, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mezun',
            name='oncekiGirisStaj',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 2, 41, 3, 970566, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ogrenci',
            name='oncekiGirisIs',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 2, 41, 3, 971558, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ogrenci',
            name='oncekiGirisStaj',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 2, 41, 3, 971558, tzinfo=utc)),
        ),
    ]
