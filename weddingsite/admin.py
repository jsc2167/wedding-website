from django.contrib import admin
from .models import Guest, RSVPFirstModel

admin.site.register(RSVPFirstModel)

class RSVPAdmin(admin.ModelAdmin):
    def name(self, obj):
        return("%s" % (obj.first_last))
    name.short_description = "Name"

    def shabbat(self, obj):
        return("%s" % (obj.shabbat_dinner))
    shabbat.short_description = "Shabbat"

    def welcome(self, obj):
        return("%s" % (obj.welcome_dinner))
    welcome.short_description = "Welcome dinner"

    def welcome_food(self, obj):
        return("%s" % (obj.welcome_dietary_restrictions))
    welcome_food.short_description = "Welcome food"

    def wed(self, obj):
        return("%s" % (obj.wedding))
    wed.short_description = "Wedding"

    def wed_food(self, obj):
        return("%s" % (obj.wedding_meal))
    wed_food.short_description = "Wedding food"

    def tuesam(self, obj):
        return("%s" % (obj.tues_am))
    tuesam.short_description = "Tues AM"


    def tuespm(self, obj):
        return("%s" % (obj.tues_pm))
    tuespm.short_description = "Tues PM"


    def song(self, obj):
        return("%s" % (obj.song_request))
    song.short_description = "Song"


    def comment(self, obj):
        return("%s" % (obj.comments))
    comment.short_description = "Comments"

    list_display = ('name', 'shabbat',
    'welcome', 'welcome_food', 'wed',
    'wed_food', 'tuesam', 'tuespm', 'song_request', 'comments')



admin.site.register(Guest, RSVPAdmin)


# class GuestInline(admin.TabularInline):
#     model = Guest
#     extra = 3
#     fields = ('name', 'attending_status', 'number_of_guests')
#
#
# class EventAdmin(admin.ModelAdmin):
#     date_hiearchy = 'date_of_event'
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'description', 'date_of_event'),
#         }),
#         ('Event Details', {
#             'fields': ('hosted_by', 'street_address', 'city', 'state', 'zip_code', 'telephone'),
#             'classes': ('collapse',)
#         })
#     )
#     inlines = [GuestInline]
#     list_display = ('title', 'date_of_event')
#     # prepopulated_fields = ('title',)
#     search_fields = ('title', 'description', 'hosted_by')
#
#
# class GuestAdmin(admin.ModelAdmin):
#     fields = ('event', 'name', 'attending_status', 'number_of_guests', 'comment')
#     list_display = ('name', 'attending_status', 'number_of_guests')
#     list_filter = ('attending_status',)
    # search_fields = ('name')


# admin.site.register(Event, EventAdmin)
# admin.site.register(Guest, GuestAdmin)
