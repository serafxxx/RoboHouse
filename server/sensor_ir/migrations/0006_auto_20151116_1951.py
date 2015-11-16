# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_ir', '0005_auto_20151116_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ircommand',
            name='name',
            field=models.CharField(default=b'', max_length=64, blank=True),
        ),
    ]
