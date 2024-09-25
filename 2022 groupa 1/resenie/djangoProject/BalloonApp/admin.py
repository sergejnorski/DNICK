from django.contrib import admin
from BalloonApp.models import Pilot, Balloon, Airline, AirlinePilot, Flight


# Register your models here.
class PilotAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')


class BalloonAdmin(admin.ModelAdmin):
    pass


class AirlinePilotInline(admin.StackedInline):
    model = AirlinePilot


class AirlineAdmin(admin.ModelAdmin):
    inlines = [AirlinePilotInline]
    list_display = ('name', )


class FlightAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Pilot, PilotAdmin)
admin.site.register(Balloon, BalloonAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flight, FlightAdmin)
