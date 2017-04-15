from django.contrib import admin
from image_cropping import ImageCroppingMixin 

from shop.models import (
    Category, SubCategory, CategoryImage, 
    Product, ProductImage,
)



class CategoryImageInline(ImageCroppingMixin, admin.TabularInline):
    model = CategoryImage
    extra = 0
    max_num = 2


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoryImageInline,
    ]    


class ProductImageInline(ImageCroppingMixin, admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
    list_filter = ('sub_category', 'sub_category__category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory)
admin.site.register(Product, ProductAdmin)