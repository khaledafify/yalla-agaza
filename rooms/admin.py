from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.User)
class Admin(admin.ModelAdmin):
    pass    
