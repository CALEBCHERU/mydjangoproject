from django.db import models

from django.urls import reverse

# Create your models here.

class ArticleModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    active = models.CharField(max_length=200)
    date = models.DateField()
    
    # def get_absolute_url(self):
    #     return reverse ("article:article-detail", kwargs=detail/int:pk/ )
        
    