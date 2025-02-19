from django.db import models


from django.contrib.auth.models import User

from django.db.models.deletion import CASCADE

# Create your models here.

class Topic(models.Model):
    
    name = models.CharField(max_length=200)
    
    
    def __str__ (self):
        return self.name



class RoomModel(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    room_name = models.CharField(max_length=100)
    description =models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    
    
    # arranges the list
    class Meta:
        ordering =['updated', 'created']
    
    def __str__(self):
        return self.room_name
    
    
    
    
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room =models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.body[0:50]
    
    
    
    