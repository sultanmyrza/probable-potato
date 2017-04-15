# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('activity', 'Activity'), ('service', 'Servis')], default=0, max_length=120, null=True, verbose_name='Event type'),
        ),
    ]
