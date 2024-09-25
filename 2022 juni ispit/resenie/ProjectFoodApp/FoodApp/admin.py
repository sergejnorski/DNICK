from django.contrib import admin

from FoodApp.models import Category, Client, Product, Sale


# Register your models here.

class ProductInline(admin.StackedInline):
    model = Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [ProductInline, ]

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', )


class ProductAdmin(admin.ModelAdmin):
    exclude = ('creator', )

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.creator == request.user:
            return True
        return False


class SaleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)