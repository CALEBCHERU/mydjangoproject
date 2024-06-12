from django.db import models

# Create your models here.


class product(models.Model):
    title = models.CharField(max_length=300,  default='Untitled' )
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300,blank=True,null=True)
    age = models.IntegerField()
    date = models.DateField()
    
    

