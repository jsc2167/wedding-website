from django.conf.urls import url
from . import views
from django.contrib import admin


# import sys
# sys.path.append("..")
from jcam import settings

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^hotels/$', views.hotels, name='hotels'),
    url(r'^registry/$', views.registry, name='registry'),
    url(r'^photos/$', views.photos, name='photos'),
    url(r'^error/$', views.error, name='error'),
    url(r'^schedule/$', views.schedule, name='schedule'),
    url(r'^sun/$', views.sun, name='sun'),
    url(r'^hop/$', views.hop, name='hop'),
    url(r'^schedule/$', views.schedule, name='schedule'),
    url(r'^sing/$', views.sing, name='sing'),
    url(r'^silk/$', views.silk, name='silk'),
    url(r'^maui/$', views.maui, name='maui'),
    url(r'^pom/$', views.pom, name='pom'),
    url(r'^cool-kids/$', views.cool_kids, name='cool-kids'),
    url(r'^nameerror/$', views.nameerror, name='nameerror'),
    url(r'^alex/$', views.alex, name='alex'),
    url(r'^cheese/$', views.cheese, name='cheese'),
    url(r'^activities/$', views.activities, name='activities'),
    url(r'^julia/$', views.julia, name='julia'),
    url(r'^ari/$', views.ari, name='ari'),
    url(r'^thanks/$', views.event_thanks, name='rsvp_event_thanks'),
    url(r'^RSVP1/$', views.RSVP1, name='rsvp1'),
    url(r'^RSVP2/$', views.RSVP2, name='rsvp2'),
    url(r'^Four_Oh_Four/$', views.Four_Oh_Four, name='Four_Oh_Four'),
    url(r'^rsvperror/$', views.RsvpError, name='rsvperror'),
    url(r'^JuliaAndAri/$', views.JuliaAndAri, name='juliaandari'),
    url(r'^admin/', admin.site.urls),
]

# urlpatterns += url('',
#         (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#     )
