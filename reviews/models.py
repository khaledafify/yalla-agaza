from django.db import models

from users import  models as user_models
from core import models as core_models
from rooms import models as room_models
# Create your models here.


class Review(core_models.TimestampedModel):

    review = models.TextField(max_length=255)
    accuracy = models.IntegerField(default=5)
    communication = models.IntegerField(default=5)
    cleanliness = models.IntegerField(default=5)
    location = models.IntegerField(default=5)
    check_in = models.IntegerField(default=5)
    value = models.IntegerField(default=5)
    user = models.ForeignKey(user_models.User,on_delete=models.CASCADE)
    room = models.ForeignKey(room_models.Room,on_delete=models.CASCADE)
    published = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.review}, [{self.room}]"