# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_importance'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shop_images/category', verbose_name='Image')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '1920x700', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
                ('for_thumb', image_cropping.fields.ImageRatioField('image', '400x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='for thumb')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.RemoveField(
            model_name='subcategoryimage',
            name='sub_category',
        ),
        migrations.DeleteModel(
            name='SubCategoryImage',
        ),
    ]
