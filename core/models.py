from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from image_cropping import ImageRatioField

# Create your models here.
LEVEL_CHOICES = (
    ('vip', 'VIP'),
    ('important', 'Important'),
)

EVENT_TYPE = (
    ('activity', 'Activity'),
    ('service', 'Servis'),
)


class Event(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False,
                             verbose_name=_('Title'))
    description = models.TextField(blank=True, null=True,
                                   verbose_name=_('Description'))
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    event_type = models.CharField(max_length=120, choices=EVENT_TYPE,
                                  default=0, null=True,
                                  verbose_name=_('Event type'))
    importance = models.CharField(max_length=120, choices=LEVEL_CHOICES,
                                  blank=True, null=True,
                                  verbose_name=_('Importance'))
    start_date = models.DateTimeField(verbose_name=_('Start date'))
    end_date = models.DateTimeField(blank=True, null=True,
                                    verbose_name=_('End date'))
    facebook_plugin = models.BooleanField(default=False,
                                          verbose_name=_('facebook message'))

    def get_image(self):
        return self.eventimage_set.first()


    def get_image_url(self):
        return self.eventimage_set.first().image.url


    def get_images(self):
        return [image.image.url for image in self.eventimage_set.all()]


    def get_day(self):
        return self.start_date.day

    def get_weekday(self):
        return self.start_date.strftime('%A')

    def get_month(self):
        return self.start_date.strftime('%B')

    # def __str__(self):
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')


class EventImage(models.Model):
    image = models.ImageField(upload_to='event_images', verbose_name=_('Image'))
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    cropping = ImageRatioField('image', '1920x700')
    facebook_ratio = ImageRatioField('image', '1200x628') # for slider
    pinterest_ratio = ImageRatioField('image', '1102x735')
    for_thumb = ImageRatioField('image', '400x300')

    # def __str__(self):
    def __unicode__(self):
        return self.event.title

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')


class Offer(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=True, null=True)
    price = models.IntegerField(default=0)
    period = models.IntegerField(default=0)
    benefits = models.TextField(blank=True)

    def get_benefits(self):
        return self.benefits.split('\n')

    def __unicode__(self):
        return self.event.title
