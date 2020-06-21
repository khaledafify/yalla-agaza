from django.db import models
from rooms import models as room_models
from users import models as user_models
from core import models as core_models


class Conversation(core_models.TimestampedModel):
    participants = models.ManyToManyField(user_models.User)

    def __str__(self):
        return f'{str(self.created)}'

class Message(core_models.TimestampedModel):
    message = models.CharField(max_length=255)
    user = models.ForeignKey(user_models.User,on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} [ {self.message} ]'
# Create your models here.
