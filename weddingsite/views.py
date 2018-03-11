from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, Http404
import datetime
import requests
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.urls import reverse
from django.template import RequestContext
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from .forms import NameForm, RSVPFirstForm, RSVPResponseForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import RSVPFirstModel, Guest

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def hotels(request):
    return render(request, 'blog/hotels.html')

def registry(request):
    return render(request, 'blog/registry.html')

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

def RsvpError(request):
    return render(request, 'blog/rsvperror.html')

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
# def RSVPInit(request):
#     rsvpform = RSVPMain(request.POST)
#     if request.method == 'POST':
#         rsvpform = RSVPMain(request.POST)
#
#         if rsvpform.is_valid():
#             # request.session['category'] = 'hop'
#             return HttpResponseRedirect('/rsvp2/')
#         else:
#             pass
#     else:
#         rsvpform = RSVPMain()
#
#     return render(request, 'blog/rsvp_init.html', {'rsvpform': rsvpform})
#
# def RSVPSecond(request):
#     if request.method == 'POST':
#         form = RSVPQuestions(request.POST)
#
#         if form.is_valid:
#             category = request.session['category']
#             return HttpResponseRedirect('/thanks/')
#         else:
#             pass
#     else:
#             form = RSVPQuestions(request.POST)
#
#     return render(request, 'blog/rsvp_second.html', {'form': form})

def RSVP1(request):

    form_class = RSVPFirstForm
    form = form_class(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            # in_database = Guest.objects.exists()
            # import pdb; pdb.set_trace()
            # if in_database == True:
            #     return HttpResponseRedirect('/nameerror/')
            # else:
            f = form.get_category()
            request.session['category'] = f
            n = form.clean_name()
            request.session['your_name'] = n
            return HttpResponseRedirect('/RSVP2/')
        else:
            form = RSVPFirstForm()
    else:
        pass
    return render(request, "blog/RSVP1.html", {'form': form})


def RSVP2(request):

    cat = request.session['category']
    form_class = RSVPResponseForm
    form = form_class(request.POST)

    if cat == 'nameerror':
        return HttpResponseRedirect('/Four_Oh_Four/')
    elif cat == 'julia':
        return HttpResponseRedirect('/JuliaAndAri')
    elif cat == 'ari':
        return HttpResponseRedirect('/JuliaAndAri')
    else:
        if request.method == 'GET':
            data = {'first_last' : request.session['your_name']}
            form = RSVPResponseForm(initial=data)
            f = form.select_questions(cat)

        if request.method == 'POST':
            # import pdb; pdb.set_trace()
            if form.is_valid():
                # Create a form instance from POST data.
                form = form_class(request.POST)
                # Save a new entry object from the form's data.
                form.save(commit=True)
                return HttpResponseRedirect('/thanks/')
            else:
                return HttpResponseRedirect('/Four_Oh_Four/')
    return render(request, "blog/RSVP2.html", {'form': form})

def Four_Oh_Four(request):

    form_class = RSVPFirstForm
    form = form_class(request.POST)

    if request.method == 'GET':
        form = RSVPFirstForm()
    if request.method == 'POST':
        form = RSVPFirstForm()
        if form.is_valid():
            f = form.get_category()
            request.session['category'] = f
            return HttpResponseRedirect('/test/')
        else:
            form = RSVPFirstForm()
    else:
        return HttpResponseRedirect('/thanks/')
    return render(request, "blog/Four_Oh_Four.html", {'form': form})

def event_thanks(request):
    return render(request, 'blog/event_thanks.html')

def JuliaAndAri(request):
    return render(request, 'blog/JuliaAndAri.html')

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
