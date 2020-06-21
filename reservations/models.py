from django.db import models
from users import models as user_models
from  core import  models as core_models
from  rooms import models as room_models
# Create your models here.


class Reservation(core_models.TimestampedModel):

    STATUS_PENDING = 'PENDING'
    STATUS_CANCELLED = 'CANCELLED'
    STATUS_CONFIRMED = 'CONFIRMED'

    STATUS_CHOICES = (
        (STATUS_PENDING,'Pending'),
        (STATUS_CONFIRMED,'Confirmed'),
        (STATUS_CANCELLED,'CANCELLED'),
    )

    status = models.CharField(max_length=12,choices=STATUS_CHOICES,default=STATUS_PENDING)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.IntegerField()
    room = models.ForeignKey(room_models.Room,on_delete=models.CASCADE)
    host = models.ForeignKey(user_models.User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.created},{self.room}'