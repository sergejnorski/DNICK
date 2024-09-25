from django.contrib import admin
from FoodApp.models import Product, Kategorija, Klient


# Register your models here.
class ProductInline(admin.StackedInline):
    model = Product
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.kreator = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.kreator:
            return True
        return False


admin.site.register(Product, ProductAdmin)


class KategorijaAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    list_display = ('ime', )
    inlines = [ProductInline, ]


admin.site.register(Kategorija, KategorijaAdmin)


class KlientAdmin(admin.ModelAdmin):
    list_display = ('ime', 'prezime')


admin.site.register(Klient, KlientAdmin)

