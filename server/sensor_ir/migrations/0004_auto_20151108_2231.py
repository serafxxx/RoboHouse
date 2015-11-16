# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_ir', '0003_auto_20151108_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ircommand',
            name='remoute',
            field=models.ForeignKey(default=None, blank=True, to='sensor_ir.IRRemoute', null=True, verbose_name=b'Remoute control'),
        ),
    ]
