from django.db import models
from backend.models import Therapist, User
# Create your models here.
class ChatModel(models.Model):
    administrator=models.ForeignKey(Therapist, on_delete=models.PROTECT)
    participants=models.ManyToManyField(User,default=None)
    token=models.CharField(max_length=1000,blank=True, null=True, default=None)
    roomID=models.CharField(max_length=500,blank=True,null=True)
    def __str__(self):
        return str(self.id)