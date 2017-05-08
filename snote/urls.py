from django.conf.urls import url

from snote import views


urlpatterns = (
    url(r'^$', views.home, name='home'),
    url(r'^(?P<node_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^(?P<node_id>[0-9]+)/notes$', views.notes, name='notes'),
)