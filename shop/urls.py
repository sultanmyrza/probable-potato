from django.conf.urls import url

from shop.views import (
        home,
        product_detail,
        category_products,
        contact_us,
    )


urlpatterns = (
    url(r'^$', home, name='home'),
    url(r'^product_detail/(?P<product_id>[0-9]+)/$', product_detail, name='product_detail'),
    url(r'^products_list/(?P<category_id>[0-9]+)/$', category_products, name='category_products'),
    url(r'^contact_us$', contact_us, name='contact_us'),
)