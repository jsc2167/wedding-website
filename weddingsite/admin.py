from django.contrib import admin
from .models import Guest, RSVPFirstModel

admin.site.register(RSVPFirstModel)

class RSVPAdmin(admin.ModelAdmin):
    list_display = ('first_last', 'shabbat_dinner',
    'welcome_dinner', 'welcome_dietary_restrictions', 'wedding',
    'wedding_meal', 'tues_am', 'tues_pm', 'song_request', 'comments')

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
