from django.contrib import admin

from BalloonApp.models import Pilot, Balloon, Airline, Flight, AirlinePilot


# Register your models here.


# За пилотите и авиокомпаниите во листата се прикажуваат само нивните имиња (и презиме за пилотот)
class PilotAdmin(admin.ModelAdmin):
    list_display = ('name', )


class BalloonAdmin(admin.ModelAdmin):
    pass


# Потребно е да овозможите додавање на објекти преку Админ панелот, со забелешка
# дека пилотите-соработници на една авиокомпанија се додаваат во делот за авиокомпанија.
class AirlinePilotInline(admin.StackedInline):
    model = AirlinePilot
    extra = 1


class AirlineAdmin(admin.ModelAdmin):
    inlines = [AirlinePilotInline]
    list_display = ('name',)


# 1. При креирањето на летот, корисникот се доделува автоматски според најавениот корисник
# 2. Откако еден лет ќе биде дефиниран и зачуван, истиот може да се промени само од корисникот кој го креирал летот
# 3. Не е дозволено бришење на летовите за ниту еден корисник
class FlightAdmin(admin.ModelAdmin):
    exclude = ('creator', )

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.creator == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Pilot, PilotAdmin)
admin.site.register(Balloon, BalloonAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flight, FlightAdmin)