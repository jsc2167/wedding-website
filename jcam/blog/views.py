from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Event
from django.http import HttpResponse, HttpResponseRedirect, Http404
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.template import RequestContext
from .forms import RSVPForm


def event_view(request, slug, model_class=Event, form_class=RSVPForm, template_name='weddingsite/event_view.html'):
    event = get_object_or_404(model_class, slug=slug)

    if request.POST:
        form = form_class(request.POST)

        if form.is_valid():
            guest = form.save()
            return HttpResponseRedirect(reverse('rsvp_event_thanks', kwargs={'slug': slug, 'guest_id': guest.id}))
    else:
        form = form_class()

    return render_to_response(template_name, {
        'event': event,
        'form': form,
    }, context_instance=RequestContext(request))


def event_thanks(request, slug, guest_id, model_class=Event, template_name='weddingsite/event_thanks.html'):
    event = get_object_or_404(model_class, slug=slug)

    try:
        guest = event.guests.get(pk=guest_id)
    except ObjectDoesNotExist:
        raise Http404

    return render_to_response(template_name, {
        'event': event,
        'guest': guest,
    }, context_instance=RequestContext(request))

def home(request):
    return render(request, 'templates/weddingsite/home.html')

def about(request):
    return render(request, 'weddingsite/about.html')

def hotels(request):
    return render(request, 'weddingsite/hotels.html')

def registry(request):
    return render(request, 'weddingsite/registry.html')

def rsvp(request):
    return render(request, 'weddingsite/rsvp.html')

def photos(request):
    return render(request, 'weddingsite/photos.html')
