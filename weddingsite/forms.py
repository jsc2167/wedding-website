from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields, CheckboxInput, ModelForm
from django.db import models
from django.utils.translation import ugettext as _
from django.core.exceptions import ObjectDoesNotExist
from .models import WEDDING_ATTENDING_CHOICES, WELCOME_CHOICES, WEDDING_CHOICES, TUES_AM_ATTENDING_CHOICES, TUES_PM_ATTENDING_CHOICES, WELCOME_ATTENDING_CHOICES, SHABBAT_ATTENDING_CHOICES, Guest, RSVPFirstModel, HOP_W_PM, COOL_KIDS_ALL, POM_WEDDING, SILK_W_S_AM, MAUI_W_S_CHOICE, SING_S_AM, SUN_W_AM, ALEX, CHEESE_W_AM_PM, JULIA, ARI
from django.forms.formsets import formset_factory
from django.forms.forms import NON_FIELD_ERRORS


class NameForm(forms.Form):

    your_name = forms.CharField(label='Your name', max_length=100)

    def clean_name(self):
        cleaned_name = self.data['your_name'].lower()
        return cleaned_name

    def get_page(self):
        cleaned_name = self.clean_name()

        if cleaned_name in HOP_W_PM:
            new_page = '/hop/'
        elif cleaned_name in COOL_KIDS_ALL:
            new_page = '/cool-kids/'
        elif cleaned_name in POM_WEDDING:
            new_page = '/pom/'
        elif cleaned_name in SILK_W_S_AM:
            new_page = '/silk/'
        elif cleaned_name in MAUI_W_S_CHOICE:
            new_page = '/maui/'
        elif cleaned_name in SING_S_AM:
            new_page = '/sing/'
        elif cleaned_name in SUN_W_AM:
            new_page = '/sun/'
        elif cleaned_name in ALEX:
            new_page = '/alex/'
        elif cleaned_name in CHEESE_W_AM_PM:
            new_page = '/cheese/'
        elif cleaned_name in JULIA:
            new_page = '/julia/'
        elif cleaned_name in ARI:
            new_page = '/ari/'
        else:
            new_page = '/nameerror/'
        return new_page

# input name, output category
class RSVPFirstForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super(RSVPFirstForm, self).__init__(*args, **kwargs)
            self.fields['your_name'].error_messages = {'required': ''}

    def clean_name(self):
        cleaned_name = self.data['your_name'].lower()
        return cleaned_name

    def get_category(self):
        cleaned_name = self.clean_name()

        if cleaned_name in HOP_W_PM:
            category = 'hop'
        elif cleaned_name in COOL_KIDS_ALL:
            category = 'cool-kids'
        elif cleaned_name in POM_WEDDING:
            category = 'pom'
        elif cleaned_name in SILK_W_S_AM:
            category = 'silk'
        elif cleaned_name in MAUI_W_S_CHOICE:
            category = 'maui'
        elif cleaned_name in SING_S_AM:
            category = 'sing'
        elif cleaned_name in SUN_W_AM:
            category = 'sun'
        elif cleaned_name in ALEX:
            category = 'alex'
        elif cleaned_name in CHEESE_W_AM_PM:
            category = 'cheese'
        elif cleaned_name in JULIA:
            category = 'julia'
        elif cleaned_name in ARI:
            category = 'ari'
        else:
            category = 'nameerror'
        return category

    class Meta:
        model = RSVPFirstModel
        fields = ['your_name']
        required=None
        label_suffix = ""


class RSVPResponseForm(forms.ModelForm):

    def select_questions(self, cat):
        if cat in ['hop', 'pom', 'sun', 'alex', 'cheese']:
            del self.fields['shabbat_dinner']
        if cat in ['pom', 'sing']:
            del self.fields['welcome_dinner']
        if cat in ['pom', 'sing']:
            del self.fields['welcome_dietary_restrictions']
        if cat in ['hop', 'pom']:
            del self.fields['tues_am']
        if cat in ['pom', 'silk', 'sing', 'sun']:
            del self.fields['tues_pm']


    class Meta:
        model = Guest
        fields = ['first_last', 'shabbat_dinner',
        'welcome_dinner', 'welcome_dietary_restrictions',
        'wedding', 'wedding_app',
        'wedding_meal', 'tues_am', 'tues_pm', 'song_request', 'comments']
        # label_suffix = ""



# class RSVPMain(forms.Form):
#
#     your_name = forms.CharField(label='Your name', max_length=100)
#
#     def clean_name(self):
#         cleaned_name = self.data['your_name'].lower()
#         return cleaned_name
#
#     def get_category(self):
#         cleaned_name = self.clean_name()
#
#         if cleaned_name in HOP_W_PM:
#             category = 'hop'
#         elif cleaned_name in COOL_KIDS_ALL:
#             category = 'cool-kids'
#         elif cleaned_name in POM_WEDDING:
#             category = 'pom'
#         elif cleaned_name in SILK_W_S_AM:
#             category = 'silk'
#         elif cleaned_name in MAUI_W_S_CHOICE:
#             category = 'maui'
#         elif cleaned_name in SING_S_AM:
#             category = 'sing'
#         elif cleaned_name in SUN_W_AM:
#             category = 'sun'
#         elif cleaned_name in ALEX:
#             category = 'alex'
#         elif cleaned_name in CHEESE_W_AM_PM:
#             category = 'cheese'
#         elif cleaned_name in JULIA:
#             category = 'julia'
#         elif cleaned_name in ARI:
#             category = 'ari'
#         else:
#             category = 'nameerror'
#         return category
#
# class RSVPQuestions(forms.Form):
#
#     def __init__(self, category):
#
#         super().__init__()
#
#         if category in ['cool_kids', 'silk', 'maui', 'sing']:
#             self.fields['shabbat'] = forms.ChoiceField(
#             label='Will you be attending the Shabbat dinner on Friday, July 20?',
#             choices=SHABBAT_ATTENDING_CHOICES, initial='',
#             widget=forms.MultipleChoiceField(attrs={'class': 'form-style'}))
#
#         if category in ['hop', 'cool_kids', 'silk', 'maui', 'sun', 'cheese']:
#             self.fields['welcome_dinner'] = forms.ChoiceField(
#             label='Will you be attending the welcome dinner on Sunday, July 22?',
#             choices=WELCOME_ATTENDING_CHOICES,
#             initial='',
#             widget=forms.RadioSelect(attrs={'class': 'form-style'}))
#
#             self.fields['welcome_dinner_food'] = forms.ChoiceField(
#             label='For the welcome dinner, I have the following dietary restrictions:',
#             choices=WELCOME_CHOICES, initial='',
#             widget=forms.RadioSelect(attrs={'class': 'form-style'}))
#
#         if category in ['hop', 'cool_kids', 'pom', 'silk', 'maui', 'sing', 'sun', 'cheese']:
#             self.fields['wedding'] = forms.ChoiceField(
#             label='Will you be joining us for the wedding ceremony and reception on Monday, July 23?',
#             choices=WEDDING_ATTENDING_CHOICES, initial='',
#             widget=forms.RadioSelect(attrs={'class': 'form-style'}))
#
#             self.fields['wedding_food'] = forms.ChoiceField(
#             label='At the wedding, I\'d like to eat',
#             choices=WEDDING_CHOICES, initial='',
#             widget=forms.RadioSelect(attrs={'class': 'form-style'}))
#
#         if category in ['cool_kids', 'silk', 'maui', 'sing', 'sun', 'cheese']:
#             self.fields['tuesday_brunch'] = forms.ChoiceField(
#             label='Will you be coming to brunch on Tuesday, July 24?',
#             choices=TUES_AM_ATTENDING_CHOICES, initial='',
#             widget=forms.RadioSelect(attrs={'class': 'form-style'}))
#
#         if category in ['hop', 'cool_kids', 'maui', 'cheese']:
#             self.fields['tuesday_night'] = forms.ChoiceField(
#             label='Will you be partying with us on Tuesday night, July 24?',
#             choices=TUES_PM_ATTENDING_CHOICES, initial='',
#             widget=forms.RadioSelect(attrs={'class': 'form-style'}))
#
#         if category in ['julia', 'ari']:
#             self.fields['iloveyou'] = forms.CharField(label='I love you', max_length=100)





# class RSVPForm(forms.Form):
#     name = forms.CharField(max_length=128)
#     attending = forms.ChoiceField(choices=VISIBLE_ATTENDING_CHOICES, initial='yes', widget=forms.RadioSelect)
#     number_of_guests = forms.IntegerField(initial=0)
#     comment = forms.CharField(max_length=100, required=False, widget=forms.Textarea)
#
#     def __init__(self, *args, **kwargs):
#         if 'guest_class' in kwargs:
#             self.guest_class = kwargs['guest_class']
#             del(kwargs['guest_class'])
#         else:
#             self.guest_class = Guest
#         super(RSVPForm, self).__init__(*args, **kwargs)
#
#     def clean_number_of_guests(self):
#         if self.cleaned_data['number_of_guests'] < 0:
#             raise forms.ValidationError(_("The number of guests you're bringing can not be negative."), code='negative_guests')
#         return self.cleaned_data['number_of_guests']
#
#     def save(self):
#         guest = self.guest_class._default_manager.get(email=self.cleaned_data['email'])
#
#         if self.cleaned_data['name']:
#             guest.name = self.cleaned_data['name']
#
#         guest.attending_status = self.cleaned_data['attending']
#         guest.number_of_guests = self.cleaned_data['number_of_guests']
#         guest.comment = self.cleaned_data['comment']
#         guest.save()
#         return guest
