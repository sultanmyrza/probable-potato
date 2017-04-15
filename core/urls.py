from django.conf.urls import url

from core.views import (home,
                        event_detail,
                        contact_us,
                        gallery,
                        blog, )

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^event_detail/(?P<event_id>[0-9]+)/$', event_detail,
        name='event_detail'),
    url(r'^gallery$', gallery, name='gallery'),
    url(r'^contact_us$', contact_us, name='contact_us'),
    url(r'^blog$', blog, name='blog'),
]
