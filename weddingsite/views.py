from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Event
from django.http import HttpResponse, HttpResponseRedirect, Http404
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.template import RequestContext

from .forms import NameForm

# def get_name(self):
#     if self.name == 'julia':
#         return render(request, 'registry.html', {'form': form})
#
#     else:
#         return render(request, 'schedule.html', {'form': form})

# def event_view(request, slug, model_class=Event, form_class=RSVPForm, template_name='blog/event_view.html'):
#     event = get_object_or_404(model_class, slug=slug)
#
#     if request.POST:
#         form = form_class(request.POST)
#
#         if form.is_valid():
#             guest = form.save()
#             return HttpResponseRedirect(reverse('rsvp_event_thanks', kwargs={'slug': slug, 'guest_id': guest.id}))
#     else:
#         form = form_class()
#
#     return render_to_response(template_name, {
#         'event': event,
#         'form': form,
#     }, context_instance=RequestContext(request))
#
#
# def event_thanks(request, slug, guest_id, model_class=Event, template_name='blog/event_thanks.html'):
#     event = get_object_or_404(model_class, slug=slug)
#
#     try:
#         guest = event.guests.get(pk=guest_id)
#     except ObjectDoesNotExist:
#         raise Http404
#
#     return render_to_response(template_name, {
#         'event': event,
#         'guest': guest,
#     }, context_instance=RequestContext(request))

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def hotels(request):
    return render(request, 'blog/hotels.html')

def registry(request):
    return render(request, 'blog/registry.html')

def rsvp(request):
    return render(request, 'blog/rsvp.html')

def photos(request):
    return render(request, 'blog/photos.html')

def error(request):
    return render(request, 'blog/error.html')

def schedule(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            new_page = form.get_page()
            return HttpResponseRedirect(new_page)
        else:
            form = NameForm()

    else:
        form = NameForm()
    return render(request, 'blog/schedule.html', {'form': form})

def sun(request):
    return render(request, 'blog/sun.html')

def hop(request):
    return render(request, 'blog/hop.html')

def sing(request):
    return render(request, 'blog/sing.html')

def silk(request):
    return render(request, 'blog/silk.html')

def maui(request):
    return render(request, 'blog/maui.html')

def pom(request):
    return render(request, 'blog/pom.html')

def cool_kids(request):
    return render(request, 'blog/cool_kids.html')

def alex(request):
    return render(request, 'blog/alex.html')

def cheese(request):
    return render(request, 'blog/cheese.html')

def nameerror(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            new_page = form.get_page()
            return HttpResponseRedirect(new_page)
        else:
            form = NameForm()

    else:
        form = NameForm()
    return render(request, 'blog/nameerror.html', {'form': form})
