from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username','email','is_host')
    list_filter = ('is_active','is_host','gender')
    fieldsets = UserAdmin.fieldsets + ( ('Customer Profile',{
        'fields': ('gender','avatar','is_host','country','currency')
    }),)




