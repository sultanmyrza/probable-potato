# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 00:17
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='cropping',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='for_thumb',
        ),
        migrations.AddField(
            model_name='productimage',
            name='promo',
            field=image_cropping.fields.ImageRatioField('image', '300x400', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='promo'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='slide',
            field=image_cropping.fields.ImageRatioField('image', '1140x362', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='slide'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='thumb',
            field=image_cropping.fields.ImageRatioField('image', '300x200', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='thumb'),
        ),
    ]
