from django.db import models

# Create your models here.

class CalebModel(models.Model):
    firstname = models.CharField(max_length=100,blank=False)
    lastname = models.CharField(max_length=100,blank=False)
    idnum = models.CharField(max_length=100,blank=False)
    phonenumber = models.CharField(max_length=100,blank=False)
    addrees = models.CharField(max_length=100,blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
# Create your models here.
class CalebFormModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add other fields as needed

    def  __str__(self):
        return f"POST: {self.name}"
