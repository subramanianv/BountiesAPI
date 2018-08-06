# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-04 01:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0006_notification_from_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='from_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='user.User'),
        ),
    ]
