from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Message)
class CustomMessageAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Conversation)
class CustomMessageAdmin(admin.ModelAdmin):
    pass
