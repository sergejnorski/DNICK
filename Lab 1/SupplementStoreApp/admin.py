from django.contrib import admin

from SupplementStoreApp import models
from SupplementStoreApp.models import Supplement


# Register your models here.


class SupplementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Supplement, SupplementAdmin)