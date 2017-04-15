from django.contrib import admin

# Register your models here.
from core.models import Event, EventImage, Offer
from image_cropping import ImageCroppingMixin 


class EventImageInline(ImageCroppingMixin, admin.TabularInline):
	model = EventImage
	extra = 0


class OfferInline(admin.TabularInline):
	model = Offer
	extra = 0


class EventAdmin(admin.ModelAdmin):
	inlines = [
		EventImageInline,
		OfferInline,
	]
	list_filter = ('event_type', 'importance')


admin.site.register(Event, EventAdmin)


from django.contrib.auth.models import User
from django.contrib.auth.models import Group
admin.site.unregister(User)
admin.site.unregister(Group)
