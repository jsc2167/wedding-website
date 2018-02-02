import datetime
from django.db import models
from django.db.models import permalink
from django.core.mail import send_mass_mail
from django.template import loader, Context
from django.conf import settings
from django.contrib.sites.models import Site


ATTENDING_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('maybe', 'Maybe'),
    ('no_rsvp', 'Hasn\'t RSVPed yet')
)


class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    date_of_event = models.DateTimeField()
    verification_code = models.CharField(max_length=32, blank=True, default='', help_text='Present for future extension/guest verification.')
    hosted_by = models.CharField(max_length=255, help_text='The name of the person/organization hosting the event.', blank=True, default='')
    street_address = models.CharField(max_length=255, help_text='The street address where the event is being held.', blank=True, default='')
    city = models.CharField(max_length=64, help_text='The city where the event is being held.', blank=True, default='')
    state = models.CharField(max_length=64, help_text='The state where the event is being held.', blank=True, default='')
    zip_code = models.CharField(max_length=10, help_text='The zip code where the event is being held.', blank=True, default='')
    telephone = models.CharField(max_length=20, blank=True, default='')
    created = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated = datetime.datetime.now()
        super(Event, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return ('rsvp_event_view', [self.slug])
    get_absolute_url = permalink(get_absolute_url)

    def guests_attending(self):
        return self.guests.filter(attending_status='yes')

    def guests_not_attending(self):
        return self.guests.filter(attending_status='no')

    def guests_may_attend(self):
        return self.guests.filter(attending_status='maybe')

    def guests_no_rsvp(self):
        return self.guests.filter(attending_status='no_rsvp')


class Guest(models.Model):
    event = models.ForeignKey(Event, related_name='guests')
    name = models.CharField(max_length=128, blank=True, default='')
    attending_status = models.CharField(max_length=32, choices=ATTENDING_CHOICES, default='no_rsvp')
    number_of_guests = models.SmallIntegerField(default=0)
    comment = models.CharField(max_length=255, blank=True, default='')
    created = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.event.title, self.attending_status)

    class Meta:
        unique_together = ('event', 'name')

    def save(self, *args, **kwargs):
        self.updated = datetime.datetime.now()
        super(Guest, self).save(*args, **kwargs)
