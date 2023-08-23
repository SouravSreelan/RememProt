from django.contrib import admin

from .models import Ciods, Publication

@admin.register(Ciods)
class CiodsAdmin(admin.ModelAdmin):
    list_display = ['name','designation']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass
