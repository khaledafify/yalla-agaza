from django.contrib import admin
from django.utils import timezone
from django.utils.safestring import mark_safe


class IsReservedRoomFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = ('Currently Reserved Reserved')

    parameter_name = 'is_reserved'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Yes'),
            ('no', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'all':
            return queryset.filter(id=r'^\d{10}$')
        if self.value() == 'yes':
            return queryset.exclude(id=r'^\d{10}$')
        if self.value() == 'no':
            return queryset.exclude(id=r'^\d{10}$')


import rooms
from . import models
from reservations import models as reservations_models
# Register your models here.



@admin.register(models.HouseRule,models.Facility,models.Amenity,models.RoomType)
class CustomRoomType(admin.ModelAdmin):
    list_display = ['name','count_rooms']
    search_fields = ['name']

    def count_rooms(self,obj):
        return obj.rooms.count()

    count_rooms.short_description = "Used By"
    pass

@admin.register(models.Photo)
class CustomPhoto(admin.ModelAdmin):
    list_display = ['caption','thumbnail','room']

    def thumbnail(self,obj):
        print(obj.file.url)
        return mark_safe(f"<img src={obj.file.url} style='width:90px;' />")
    pass

class CustomPhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class CustomRoom(admin.ModelAdmin):
    inlines = (CustomPhotoInline,)
    raw_id_fields = ['host']
    list_filter = ['instant_book','room_type' , 'city','country','facilities']
    search_fields = ['host__email','host__username','name','description']
    list_display = ['name','room_type','is_reserved','photos_count','facilities_count',
                    'house_rules_count', 'amenities_count','photos_count','instant_book']

    fieldsets =  ( ('Basic Information',{
        'fields': ('name','description','room_type','country','price','address')
    }),('Advanced Information',{
        'fields': ('guests','beds','bedrooms','baths',)
    }),('Time Management',{
        'fields': ('check_in','check_out',)
    }),('Property Setup',{
        'fields': ('amenities','facilities','house_rules')
    }),('Owner Preference',{
        'fields': ('host','instant_book')
    }),)

    filter_horizontal = ['house_rules','amenities','facilities']

    def facilities_count(self, obj):
        return obj.facilities.count()

    def house_rules_count(self, obj):
        return obj.house_rules.count()

    def amenities_count(self,obj):
        return obj.amenities.count()

    def photos_count(self,obj):
        return models.Photo.objects.filter(room_id=obj.id).all().count()

    def is_reserved(self,obj):
        is_reserved = reservations_models.Reservation.objects.filter(room_id=obj.id,status=reservations_models.Reservation.STATUS_CONFIRMED,check_in__gte=timezone.now().date()).all().count()
        return True if is_reserved > 0 else False

    facilities_count.short_description = 'Facilities Count'
    house_rules_count.short_description = 'House Rules Count'
    amenities_count.short_description = 'Amenities Count'
    photos_count.short_description = "Photos Count"
    is_reserved.short_description = 'Reserved'
    is_reserved.boolean = True


    pass