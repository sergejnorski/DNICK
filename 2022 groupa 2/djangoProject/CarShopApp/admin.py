from django.contrib import admin

from CarShopApp.models import Car, CarShop, Manufacturer, Fix, CarShopManufacturer


# Register your models here.

# За автомобилите се прикажува типот и дозволената брзина
# и се филтрира според прозиведувач
class CarAdmin(admin.ModelAdmin):
    list_display = ('type', 'max_speed')
    list_filter = ('manufacturer', )


class CarShopManufacturerAdmin(admin.StackedInline):
    model = CarShopManufacturer


class CarShopAdmin(admin.ModelAdmin):
    inlines = [CarShopManufacturerAdmin]

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


#  Само супер корисник може да додава производители на автомобили
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', )

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False


class FixAdmin(admin.ModelAdmin):
    exclude = ('car_owner', )

    def save_model(self, request, obj, form, change):
        obj.car_owner = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Car, CarAdmin)
admin.site.register(CarShop, CarShopAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Fix, FixAdmin)
