# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='importance',
            field=models.CharField(blank=True, choices=[('vip', 'VIP'), ('important', 'Important')], max_length=120, null=True, verbose_name='Importance'),
        ),
    ]