from django import forms
from django.core.exceptions import ValidationError

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
    'alex wiltschko', 'katherine gorman', 'ryan heisler', 'etta king',]

COOL_KIDS_ALL = ['rebecca caine', 'john light', 'ben caine', 'anna caine']

POM_WEDDING = ['raphael koster', 'avi ruderman', 'priya ruderman',
'francis song', 'sam ritter', 'samuel ritter', 'cotie long', 'kim stachenfeld',
'kimberly stachenfeld', 'neil rabinowitz', 'jo rabinowitz',]

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
        else:
            new_page = '/nameerror/'
        return new_page


        # from django.utils.translation import ugettext as _
        # from django import forms
        # from django.core.exceptions import ObjectDoesNotExist
        # from .models import ATTENDING_CHOICES, Guest
        #
        #
        # VISIBLE_ATTENDING_CHOICES = [choice for choice in ATTENDING_CHOICES if choice[0] != 'no_rsvp']
        #
        #
        # class RSVPForm(forms.Form):
        #     email = forms.EmailField()
        #     name = forms.CharField(max_length=128)
        #     attending = forms.ChoiceField(choices=VISIBLE_ATTENDING_CHOICES, initial='yes', widget=forms.RadioSelect)
        #     number_of_guests = forms.IntegerField(initial=0)
        #     comment = forms.CharField(max_length=255, required=False, widget=forms.Textarea)
        #
        #     def __init__(self, *args, **kwargs):
        #         if 'guest_class' in kwargs:
        #             self.guest_class = kwargs['guest_class']
        #             del(kwargs['guest_class'])
        #         else:
        #             self.guest_class = Guest
        #         super(RSVPForm, self).__init__(*args, **kwargs)
        #
        #     def clean_email(self):
        #         try:
        #             guest = self.guest_class._default_manager.get(email=self.cleaned_data['email'])
        #         except ObjectDoesNotExist:
        #             raise forms.ValidationError(_('That e-mail is not on the guest list.'), code='not_on_list')
        #
        #         if hasattr(guest, 'attending_status') and guest.attending_status != 'no_rsvp':
        #             raise forms.ValidationError(_('You have already provided RSVP information.'), code='already_rsvp')
        #
        #         return self.cleaned_data['email']
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
