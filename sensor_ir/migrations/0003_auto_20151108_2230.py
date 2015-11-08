# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_ir', '0002_auto_20151108_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ircommand',
            name='remoute',
            field=models.ForeignKey(default=None, verbose_name=b'Remoute control', blank=True, to='sensor_ir.IRRemoute'),
        ),
    ]
