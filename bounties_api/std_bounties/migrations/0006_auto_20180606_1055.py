# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('std_bounties', '0005_auto_20180503_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='BountyDraft',
            fields=[
                ('bounty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='std_bounties.Bounty')),
                ('on_chain', models.BooleanField(default=False)),
            ],
            bases=('std_bounties.bounty',),
        ),
        migrations.AddField(
            model_name='bounty',
            name='difficulty',
            field=models.IntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Advanced')], null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='identifier',
            field=models.UUIDField(null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='revisions',
            field=models.IntegerField(null=True),
        ),
    ]
