from django.conf.urls import url
from . import views

# import sys
# sys.path.append("..")
from jcam import settings

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^hotels/$', views.hotels, name='hotels'),
    url(r'^registry/$', views.registry, name='registry'),
    # url(r'^rsvp/$', views.rsvp, name='rsvp'),
    url(r'^photos/$', views.photos, name='photos'),
    url(r'^error/$', views.error, name='error'),
    # url(r'^rsvp/(?P<slug>[A-Za-z0-9_-]+)/$', views.event_view, name='rsvp_event_view'),
    # url(r'^rsvp/(?P<slug>[A-Za-z0-9_-]+)/thanks/(?P<guest_id>\d+)/$', views.event_thanks, name='rsvp_event_thanks'),
]

# urlpatterns += url('',
#         (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#     )
