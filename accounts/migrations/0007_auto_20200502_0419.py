# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-02 01:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200429_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mezun',
            name='oncekiGirisIs',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 1, 19, 29, 460115, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mezun',
            name='oncekiGirisStaj',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 1, 19, 29, 460115, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ogrenci',
            name='gorulenIsId',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ogrenci',
            name='gorulenStajId',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ogrenci',
            name='ilanToplam',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ogrenci',
            name='oncekiGirisIs',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 1, 19, 29, 461114, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ogrenci',
            name='oncekiGirisStaj',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 1, 19, 29, 461114, tzinfo=utc)),
        ),
    ]
