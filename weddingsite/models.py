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
    ('1', 'None'),
    ('2', 'Vegetarian'),
    ('3', 'Vegan'),
    ('4', 'Gluten-free'),
    ('5', 'No meat with milk'),
    ('6', 'Other'),
)

WEDDING_CHOICES = (
    ('1', 'Ricotta and spinach malfatti with sage butter and parmesan crisps',),
    ('2', 'Red lentil coconut curry, grilled sweetcorn and courgette, and crisp rice balls'),
)

class TestModel(models.Model):
    name = models.TextField(max_length=128, unique=True)
    category = models.CharField(max_length=20, null=True, blank=True)
    shabbat_dinner = models.NullBooleanField(default=None)
    welcome_dinner = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Party(models.Model):
    """
    A party consists of one or more guests.
    """
    name = models.TextField()
    category = models.CharField(max_length=20, null=True, blank=True)
    shabbat_dinner = models.NullBooleanField(default=None)
    welcome_dinner = models.BooleanField(default=False)
    wedding = models.NullBooleanField(default=None)
    tues_am = models.NullBooleanField(default=None)
    tues_pm = models.NullBooleanField(default=None)
    comments = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return 'Party: {}'.format(self.name)

    @classmethod
    def in_default_order(cls):
        return cls.objects.order_by('category', 'name')

    @property
    def ordered_guests(self):
        return self.guest_set.order_by('is_child', 'pk')

    @property
    def any_guests_attending(self):
        return any(self.guest_set.values_list('is_attending', flat=True))


class Guest(models.Model):
    """
    A single guest
    """
    first_name = models.TextField()
    last_name = models.TextField()
    shabbat_dinner = models.NullBooleanField(default=None)
    welcome_dinner = models.NullBooleanField(default=None)
    welcome_dietary_restrictions = models.CharField(max_length=6,
    choices=WELCOME_CHOICES, default='1')
    wedding = models.NullBooleanField(default=None)
    wedding_meal = models.CharField(max_length=2,
    choices=WEDDING_CHOICES, default='1')
    tues_am = models.NullBooleanField(default=None)
    tues_pm = models.NullBooleanField(default=None)

    @property
    def name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def __unicode__(self):
        return 'Guest: {} {}'.format(self.first_name, self.last_name)
