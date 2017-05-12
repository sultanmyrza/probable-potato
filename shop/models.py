from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from image_cropping import ImageRatioField


LEVEL_CHOICES = (
    ('vip', 'VIP'),
    ('important', 'Important'),
)


class Category(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False,
                              verbose_name=_('Title'))
    
    def __unicode__(self):
        return self.title

    def get_image(self):
        return self.categoryimage_set.first()

    def get_images(self):
        return self.categoryimage_set.all()

    def get_image_urls(self):
        return [image.image.url for image in self.categoryimage_set.all()]


class CategoryImage(models.Model):
    image = models.ImageField(upload_to='shop_images/category', verbose_name=_('Image'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cropping = ImageRatioField('image', '1920x700')
    for_thumb = ImageRatioField('image', '400x300') 

    # def __str__(self):
    def __unicode__(self):
        return self.category.title

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=False, null=False,
                              verbose_name=_('Title'))
    description = models.TextField(blank=True, null=True, 
                                   verbose_name=_('Description'))
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    facebook_plugin = models.BooleanField(default=False, 
                                          verbose_name=_('facebook message'))
    price = models.FloatField()
    importance = models.CharField(max_length=120, choices=LEVEL_CHOICES,
                                  blank=True, null=True,
                                  verbose_name=_('Importance'))

    def get_image(self):
        return self.productimage_set.first()

    def get_images(self):
        return self.productimage_set.all()

    def get_image_urls(self):
        return [image.image.url for image in self.productimage_set.all()]

    # def __str__(self):
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductImage(models.Model):
    image = models.ImageField(upload_to='shop_images/product', verbose_name=_('Image'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    carousel = ImageRatioField('image', '640x362')
    promo = ImageRatioField('image', '300x400')
    thumb = ImageRatioField('image', '300x200')
    grid = ImageRatioField('image', '255x170')

    # def __str__(self):
    def __unicode__(self):
        return self.product.title

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')