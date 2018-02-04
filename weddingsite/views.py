from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, Http404
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.template import RequestContext
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from .forms import NameForm, RSVPMain, RSVPQuestions
import csv

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def hotels(request):
    return render(request, 'blog/hotels.html')

def registry(request):
    return render(request, 'blog/registry.html')

# def rsvp(request):
#     return render(request, 'blog/rsvp.html')

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

def activities(request):
    return render(request, 'blog/activities.html')

def julia(request):
    return render(request, 'blog/julia.html')

def ari(request):
    return render(request, 'blog/ari.html')

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

#make RSVP form save responses to database
def RSVPInit(request):
    rsvpform = RSVPMain(request.POST)
    if request.method == 'POST':
        rsvpform = RSVPMain(request.POST)

        if rsvpform.is_valid():
            request.session['category'] = rsvpform.get_category()
            return HttpResponseRedirect('/rsvp2/')
        else:
            pass
    else:
        rsvpform = RSVPMain()

    return render(request, 'blog/rsvp_init.html', {'rsvpform': rsvpform})

def RSVPSecond(request):
    form = RSVPQuestions(request.POST)
    if request.method == 'POST':
        form = RSVPQuestions(request.POST)

        if form.is_valid:
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            # welcome_dinner = request.POST.get('welcome_dinner', '')
            # download_dir = "rsvp_responses.csv"
            # csv = open(download_dir, "a")
            # csv.write(welcome_dinner)
            return HttpResponseRedirect('/thanks/')
        else:
            pass
    else:
        form = RSVPQuestions(request.session['category'])

    return render(request, 'blog/rsvp_second.html', {'form': form})


def event_thanks(request):
    return render(request, 'blog/event_thanks.html')


# def rsvp(request, model_class=Event, form_class=RSVPForm, template_name='blog/rsvp.html'):
#     event = get_object_or_404(model_class)
#
#     if request.POST:
#         rsvpform = form_class(request.POST)
#
#         if rsvpform.is_valid():
#             guest = rsvpform.save()
#             return HttpResponseRedirect(reverse('rsvp_event_thanks'))
#     else:
#         rsvpform = form_class()
#
#     return render_to_response(template_name, {
#         'event': event,
#         'rsvpform': rsvpform,
#     }, context_instance=RequestContext(request))
#
#
# def event_thanks(request, model_class=Event, template_name='blog/event_thanks.html'):
#     event = get_object_or_404(model_class)
#
#     try:
#         guest = event.guests.get
#     except ObjectDoesNotExist:
#         raise Http404
#
#     return render_to_response(template_name, {
#         'event': event,
#         'guest': guest,
#     }, context_instance=RequestContext(request))
