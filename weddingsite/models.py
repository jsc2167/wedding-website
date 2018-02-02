from django.utils import timezone
import datetime
from django.db import models
from django.db.models import permalink
from django.core.mail import send_mass_mail
from django.template import loader, Context
from django.conf import settings
from django.contrib.sites.models import Site


SHABBAT_ATTENDING_CHOICES = (
    ('yes', 'Don\'t be meshuga, of course I\'ll be there!'),
    ('no', 'Az och un vai! I can\'t make it!')
)

WELCOME_ATTENDING_CHOICES = (
    ('yes', 'Definitely!'),
    ('no', 'I won\'t be able to make it')
)

WEDDING_ATTENDING_CHOICES = (
    ('yes', 'Joyfully accept'),
    ('no', 'Regretfully decline'),
)

TUES_AM_ATTENDING_CHOICES = (
    ('yes', 'I love brunch! Count me in!'),
    ('no', 'I won\'t be able to make it.'),
)

TUES_PM_ATTENDING_CHOICES = (
    ('yes', 'Fo\' sho\''),
    ('no', 'I\'ve got other places to be')
)

WELCOME_CHOICES = (
    ('1', 'Fish'),
    ('2', 'Steak'),
    ('3', 'Veggie')
)

WEDDING_CHOICES = (
    ('1', 'Ricotta and spinach malfatti with sage butter and parmesan crisps',),
    ('2', 'Red lentil coconut curry, grilled sweetcorn and courgette, and crisp rice balls'),
)
#
# class Event(models.Model):
#     tuesday_am = forms.ChoiceField(label='Tuesday brunch', choices=ATTENDING_CHOICES, initial='yes', widget=forms.RadioSelect)
#
#     def __unicode__(self):
#         return self.title
#
#     def save(self, *args, **kwargs):
#         self.updated = datetime.datetime.now()
#         super(Event, self).save(*args, **kwargs)
#
#     def guests_attending(self):
#         return self.guests.filter(attending_status='yes')
#
#     def guests_not_attending(self):
#         return self.guests.filter(attending_status='no')


# class Guest(models.Model):
#     tuesday_am = models.ForeignKey(Event, related_name='guests', on_delete=models.CASCADE,)
#     name = models.CharField(max_length=128, blank=True, default='')
#     attending_status = models.NullBooleanField(default=None)
#     number_of_guests = models.SmallIntegerField(default=0)
#     meal = models.CharField(max_length=100, choices=MEALS, null=True, blank=True)
#
#     # def __unicode__(self):
#     #     return u"%s - %s - %s" % (self.event.title, self.email, self.attending_status)
#
#     class Meta:
#         unique_together = ('attending_status', 'name')
#
#     def save(self, *args, **kwargs):
#         self.updated = datetime.datetime.now()
#         super(Guest, self).save(*args, **kwargs)
