from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Review)
class CustomReviewAdminModel(admin.ModelAdmin):
    list_display = ['room','user','published','accuracy','value','check_in','location',
                    'cleanliness','communication','avg_rating']

    raw_id_fields = ['user']

    list_filter = ['published','room__city','accuracy','cleanliness','check_in','location',
                   'communication','value']

    search_fields = ['review','room__name','room__host__email',]