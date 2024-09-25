from django.contrib import admin

from EventApp.models import BandEvent, Band, Event


# Register your models here.


class BandEventInline(admin.StackedInline):
    model = BandEvent
    extra = 1


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', )


# Настани може да додаваат само супер-корисници, и тие автоматски се доделуваат на настанот
# Настаните не може да се бришат и менуваат, освен од нивниот корисник-креатор
class EventAdmin(admin.ModelAdmin):
    inlines = [BandEventInline, ]
    list_display = ('name', 'date_time')
    exclude = ('creator', )

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.creator:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.creator:
            return True
        return False


admin.site.register(Band, BandAdmin)
admin.site.register(Event, EventAdmin)

