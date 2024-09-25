from django.contrib import admin

from EventsApp.models import Event, Band, BandEvent


# Register your models here.

class BandEventAdmin(admin.StackedInline):
    model = BandEvent


class EventAdmin(admin.ModelAdmin):
    inlines = [BandEventAdmin, ]
    list_display = ('ime', 'vremeOdrzuvanje', )
    exclude = ('kreator', )

    def save_model(self, request, obj, form, change):
        obj.kreator = request.user
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.kreator:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.kreator:
            return True
        return False


class BandAdmin(admin.ModelAdmin):
    list_display = ('ime', 'imeDrzava', )


admin.site.register(Event, EventAdmin)
admin.site.register(Band, BandAdmin)