# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 00:22
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20170512_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='carousel',
            field=image_cropping.fields.ImageRatioField('image', '960x362', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='carousel'),
        ),
    ]