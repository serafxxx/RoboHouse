# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IRModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=64, verbose_name=b'Sensor name', blank=True)),
                ('ip', models.GenericIPAddressField(protocol=b'IPv4', verbose_name=b'IP address')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
