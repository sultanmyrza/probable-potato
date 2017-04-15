from django.shortcuts import render, get_object_or_404
from core.models import Event, EVENT_TYPE


# Create your views here.
def home(request):
	events = Event.objects.all()
	last_events = events.order_by('-timestamp')[:3]
	vip_events = events.filter(importance='vip')
	important_events = events.filter(importance='important')
	services = events.filter(event_type='service')
	context = {
		'events': events,
		'important_events': important_events,
		'vip_events': vip_events,
		'last_events': last_events,
		'services': services,
		'event_types': EVENT_TYPE,
	}
	return render(request, 'core/index.html', context)


def event_detail(request, event_id):
	events = Event.objects.all()
	try:
		event = events.get(id=event_id)
	except :
		event = None
	last_events = events.order_by('-timestamp')[:3]
	services = events.filter(event_type='service')
	context = {
		'event': event,
		'last_events': last_events,
		'services': services,
	}
	return render(request, 'core/event_detail.html', context)


def contact_us(request):
	context = {}
	return render(request, 'core/contact.html', context)


def gallery(request):
	context = {
		'events': Event.objects.all(),
		'event_types': EVENT_TYPE, 
	}
	return render(request, 'core/gallery.html', context)


def blog(request):
	events = Event.objects.all()
	last_events = events.order_by('-timestamp')[:3]
	services = events.filter(event_type='service')
	context = {
		'events': events,
		'last_events': last_events,
		'services': services,
	}
	return render(request, 'core/blog.html', context)