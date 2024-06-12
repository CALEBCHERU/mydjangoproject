from .models import ArticleModel
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields =[
            'title',
            'content',
            'active',
            'date'
        ]
        