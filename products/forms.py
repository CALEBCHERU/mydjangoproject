from django import forms

from .models import product





class productform (forms.ModelForm):
    class Meta:
        model = product
        fields =[
            'title',
            'name',
            'age',
            'description',
            'date'
        ]
        
    def claen_title(self):
        title = self.cleaned_data.get("title")
        if not "CEO" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "Caleb" in title:
            raise forms.ValidationError("The name should be Caleb ")
        return title

#the  code below helps  us to print data of then databse to the website 
class RawProduct(forms.Form):
    title = forms.CharField()
    name = forms.CharField()
    age = forms.IntegerField()
    description = forms.CharField( widget= forms.Textarea(attrs={
        "class":"class1",
        "id": "my_id_for_textarea"
        
    }))
    date = forms.DateField()
    
    

    