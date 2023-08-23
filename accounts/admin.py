from django.contrib import admin
from .models import UserBase

@admin.register(UserBase)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username','created']

