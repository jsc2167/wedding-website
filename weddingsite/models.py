from django.utils import timezone
import datetime
from django.db import models
from django.db.models import permalink
from django.core.mail import send_mass_mail
from django.template import loader, Context
from django.conf import settings
from django.contrib.sites.models import Site
# from .forms import HOP_W_PM, COOL_KIDS_ALL, POM_WEDDING, SILK_W_S_AM,
# MAUI_W_S_CHOICE, SING_S_AM, SUN_W_AM, ALEX, CHEESE_W_AM_PM, JULIA, ARI

HOP_W_PM = [
    'rachel insoft', 'phil masui', 'philip masui', 'mary awadallah',
    'mary shehata', 'michael shehata', 'mike shehata', 'christina amendola',
    'chrissy amendola', 'vince gaviria', 'vincent gaviria',
    'amanda delshad', 'amanda mintzer', 'danny mintzer',
    'celeste conrad', 'celeste holmes', 'jay holmes', 'ashley budasoff',
    'larry budasoff', 'lawrence budasoff', 'adin insoft',
    'leah kandel', 'jacob newman', 'kendrice newman',
    'kendrice james', 'clay thibodeaux', 'tari tan', 'taralyn tan'
    'ian mclachlan', 'milner', 'elliott milner',
    'e. s. milner', 'e s milner', 'saul glasman', 'nicole neubarth',
    'alan emanuel', 'kaori graybeal', 'matthias minderer',
    'christina welsh', 'dan millman', 'daniel millman', 'rebecca yang',
    'alex wiltschko', 'katherine gorman', 'ryan heisler', 'etta king',
    'etta heisler']

COOL_KIDS_ALL = ['rebecca caine', 'john light', 'ben caine', 'anna caine']

POM_WEDDING = ['raphael koster', 'avi ruderman', 'priya ruderman',
'francis song', 'sam ritter', 'samuel ritter', 'cotie long', 'kim stachenfeld',
'kimberly stachenfeld', 'neil rabinowitz', 'jo rabinowitz', 'sonia rego',
'matt kusner', 'matthew kusner']

SILK_W_S_AM = ['claire caine', 'dan caine', 'daniel caine', 'jerome socolovsky',
'petra glimaker', 'emanuel socolovsky', 'shoshi socolovsky', 'shosh socolovsky',
'eviatar socolovsky', 'yaara socolovsky', 'caroline ertz', 'greg ertz',
'maria socolovsky']

MAUI_W_S_CHOICE = ['mendel socolovsky', 'nils socolovsky', 'eviatar socolovsky',
'ronli socolovsky', 'ron li socolovsky', 'tomer socolovsky']

SING_S_AM = ['janet tanzi', 'dena glasgow', 'jason glasgow', 'heather zacker',
'david harlow', 'sheryl marcus', 'alan marcus', 'marcia leifer', 'alan leifer',
'wes gardenswartz', 'wesley gardenswartz', 'shira gardenswartz', 'merle hass',
'sylvain korzennik', 'sue bergman', 'barry bergman', 'susan bergman',
'vicki isman', 'marshall isman', 'michael kane', 'sue kane', 'bob wake',
'marcia wake', 'beth davis', 'maerton davis']

SUN_W_AM = ['rob insoft', 'robert insoft', 'andie insoft', 'tova morcos',
'samir morcos', 'jared kliger', 'philip freed', 'linda freed',
'linda rich freed', 'linda rich', 'chris harvey', 'christopher harvey',
'lauren orefice', 'shalva greenbaum']

ALEX = ['alex trott', 'alexander trott']

CHEESE_W_AM_PM = ['dahlia greenbaum', 'daniel greenbaum',]

JULIA = ['julia caine']

ARI = ['ari morcos']

SHABBAT_ATTENDING_CHOICES = (
    (True, 'Don\'t be meshuga, of course I\'ll be there!'),
    (False, 'Az och un vai! I can\'t make it!')
)

WELCOME_ATTENDING_CHOICES = (
    (True, 'Definitely!'),
    (False, 'I won\'t be able to make it')
)

WEDDING_ATTENDING_CHOICES = (
    (True, 'Joyfully accept'),
    (False, 'Regretfully decline'),
)

TUES_AM_ATTENDING_CHOICES = (
    (True, 'I love brunch! Count me in!'),
    (False, 'I won\'t be able to make it.'),
)

TUES_PM_ATTENDING_CHOICES = (
    (True, 'Fo\' sho\''),
    (False, 'I\'ve got other places to be')
)

WELCOME_CHOICES = (
    ('None', 'None'),
    ('Veggie', 'Vegetarian'),
    ('Vegan', 'Vegan'),
    ('GF', 'Gluten-free'),
    ('Kosh', 'No meat with milk'),
    ('Other', 'Other (please elaborate in comments section)'),
)

WEDDING_CHOICES = (
    ('malfatti', 'Ricotta and spinach malfatti with sage butter and parmesan crisps (vegetarian)',),
    ('curry', 'Red lentil coconut curry, grilled sweetcorn and courgette, and crisp rice balls (vegan)'),
)


class RSVPFirstModel(models.Model):
    your_name = models.CharField(default=None, max_length=100)

    def __unicode__(self):
        return u"%s" % (self.your_name)

class GuestManager(models.Manager):
    def in_db(self):
        nm = self.filter(first_last='your_name').exists()
        return nm


class Guest(models.Model):
    """
    A single guest
    """
    app_label = 'weddingsite'
    first_last = models.CharField(verbose_name='Your name:', blank=True,
    default='%s', max_length=128)
    shabbat_dinner = models.NullBooleanField(choices=SHABBAT_ATTENDING_CHOICES, verbose_name=
    '\nWill you be able to attend Shabbat dinner on Friday, July 20th?\n\n',
    default=True, blank=True)
    welcome_dinner = models.NullBooleanField(choices=WELCOME_ATTENDING_CHOICES, max_length=20, verbose_name=
    '\nWill you be able to attend the welcome dinner on Sunday, July 22nd?\n\n',
    default=True, blank=True)
    welcome_dietary_restrictions = models.CharField(verbose_name=
    '\nDo you have any dietary restrictions?\n\n', max_length=6,
    choices=WELCOME_CHOICES, default='None', blank=True)
    wedding = models.NullBooleanField(verbose_name=
    '\nWill you be able to attend the wedding on Monday, July 23rd?\n\n',
    default=True, blank=True)
    wedding_meal = models.CharField(verbose_name=
    '\nAt the wedding, I would like to eat:\n\n', max_length=200,
    choices=WEDDING_CHOICES, default='malfatti', blank=True)
    tues_am = models.NullBooleanField(
    verbose_name='\nWill you be able to come to brunch on Tuesday, July 24th?\n\n',
    default=True, blank=True)
    tues_pm = models.NullBooleanField(
    verbose_name='\nWill you be able to come to the gathering on Tuesday, July 24th?\n\n',
    default=True, blank=True, )
    song_request = models.TextField(
    verbose_name='I would dance if I heard this song:', default = 'YMCA by The Village People',
    blank=True, max_length=2048)
    comments = models.TextField(
    verbose_name='Comments for the couple!', default='I\'m so excited to come!',
    blank=True, max_length=2048, )

    @property
    def name(self):
        return u'{}'.format(self.first_last)

    def __unicode__(self):
        return 'Guest: {}'.format(self.first_last)

    # objects = GuestManager()



# class Party(models.Model):
#     """
#     A party consists of one or more guests.
#     """
#     name = models.TextField()
#     category = models.CharField(max_length=20, null=True, blank=True)
#     shabbat_dinner = models.NullBooleanField(default=None)
#     welcome_dinner = models.BooleanField(default=False)
#     wedding = models.NullBooleanField(default=None)
#     tues_am = models.NullBooleanField(default=None)
#     tues_pm = models.NullBooleanField(default=None)
#     comments = models.TextField(null=True, blank=True)
#
#     def __unicode__(self):
#         return 'Party: {}'.format(self.name)
#
#     @classmethod
#     def in_default_order(cls):
#         return cls.objects.order_by('category', 'name')
#
#     @property
#     def ordered_guests(self):
#         return self.guest_set.order_by('is_child', 'pk')
#
#     @property
#     def any_guests_attending(self):
#         return any(self.guest_set.values_list('is_attending', flat=True))
