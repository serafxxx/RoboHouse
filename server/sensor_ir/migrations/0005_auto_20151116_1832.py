# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_ir', '0004_auto_20151108_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='ircommand',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 16, 18, 32, 59, 962850), verbose_name=b'Creation date', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ircommand',
            name='encoding',
            field=models.CharField(default=b'', max_length=64, verbose_name=b'Command encoding'),
        ),
        migrations.AlterField(
            model_name='ircommand',
            name='code',
            field=models.CharField(default=b'', max_length=64, verbose_name=b'Command hex code'),
        ),
    ]
