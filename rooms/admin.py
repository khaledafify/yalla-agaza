from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.RoomType)
class CustomRoomType(admin.ModelAdmin):
    pass

@admin.register(models.Amenity)
class CustomRoomType(admin.ModelAdmin):
    pass


@admin.register(models.Facility)
class CustomRoomType(admin.ModelAdmin):
    pass

@admin.register(models.HouseRule)
class CustomRoomType(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class CustomRoom(admin.ModelAdmin):
    pass

@admin.register(models.Photo)
class CustomPhoto(admin.ModelAdmin):
    pass