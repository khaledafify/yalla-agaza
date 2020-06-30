from django.db import models
# Create your models here.
from django_countries.fields import CountryField
import datetime
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimestampedModel):
    name = models.CharField(default='',max_length=100)

    class Meta:
        abstract = True

class RoomType(AbstractItem):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Room Type'
        ordering = ['-name']
    pass

class Amenity(AbstractItem):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Amenties'
    pass

class Facility(AbstractItem):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Facilities'
        ordering = ['-created']
    pass

class HouseRule(AbstractItem):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'House Rule'


    pass



class Room(core_models.TimestampedModel):
    name = models.CharField(max_length=255,default='')
    description = models.TextField(default='e')
    country = CountryField(default="EG")
    city = models.CharField(max_length=80,default='')
    price = models.DecimalField(max_digits=5,decimal_places=2,default=100)
    address = models.CharField(default= '' ,max_length=255)
    guests = models.IntegerField(null=False,blank=False,default=0)
    beds = models.IntegerField(default=1,null=False,blank=False)
    bedrooms = models.IntegerField(default=1)
    baths = models.IntegerField(default=1,null=False,blank=False)
    check_in = models.TimeField(default=None)
    check_out = models.TimeField(default=None)
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User,on_delete=models.CASCADE,default=None)
    room_type = models.ForeignKey(RoomType,related_name='rooms',blank=True,null=True,on_delete=models.SET_NULL)
    amenities = models.ManyToManyField(Amenity,blank=True,related_name='rooms')
    facilities = models.ManyToManyField(Facility,blank=True,related_name='rooms')
    house_rules = models.ManyToManyField(HouseRule,blank=True,related_name='rooms')

    def __str__(self):
        return self.name

class Photo(core_models.TimestampedModel):
    caption = models.CharField(max_length=100)
    file = models.ImageField()
    room = models.ForeignKey(Room,on_delete=models.CASCADE)

