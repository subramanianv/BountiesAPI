# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-31 18:54
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20180717_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
