from django.contrib import admin
from image_cropping import ImageCroppingMixin 

from shop.models import (
    Category, CategoryImage,
    Product, ProductImage,
)


class ProductInline(ImageCroppingMixin, admin.TabularInline):
    model = Product
    extra = 0
    max_num = 2


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        # ProductInline,
    ]



class ProductImageInline(ImageCroppingMixin, admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
    list_filter = ('category',)
    list_display = ('id', 'title',  'price', 'importance')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)