
from django.contrib import admin
from django.utils import timezone

from . import models
# Register your models here.


@admin.register(models.Reservation)
class ReservationCustomAdminModel(admin.ModelAdmin):
    list_display = ['room','status','check_in','check_out','is_reserved','room_price']
    raw_id_fields = [
        'room',
        'host'
    ]

    list_filter = ['check_in','check_out','status']
    search_fields = ['room__name','room__host__username','room__host__email']
    def is_reserved(self,obj):
        is_reserved = models.Reservation.objects.filter(pk=obj.id,status=models.Reservation.STATUS_CONFIRMED,check_in__gte=timezone.now().date()).all().count()
        return True if is_reserved > 0 else False


    def room_price(self,obj):
        room_cost = obj.room.price
        return room_cost

    is_reserved.short_description = "Currently Reserved"
    is_reserved.boolean = True
    room_price.short_description = "Cost"



