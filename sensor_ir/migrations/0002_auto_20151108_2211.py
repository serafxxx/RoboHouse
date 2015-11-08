# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_ir', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IRCommand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=64, verbose_name=b'Command hex code')),
            ],
        ),
        migrations.CreateModel(
            name='IRRemoute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='ircommand',
            name='remoute',
            field=models.ForeignKey(verbose_name=b'Remoute control', to='sensor_ir.IRRemoute', null=True),
        ),
    ]
