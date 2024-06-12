
from django.forms import ModelForm
from calebform.models import CalebModel,CalebFormModel
from django import forms

class CalebForm(forms.ModelForm):
    firstname =  forms.CharField(
        widget= forms.TextInput(attrs={ "placeholder": "firstname"})
        
    )
    
    def clean_idnum(self):
        idnum = self.cleaned_data.get("idnum")
        idnuml = len(idnum)
        if idnuml >= 8:
            return(idnum)
        else:
            raise forms.ValidationError("The id number should be 8 digits")
    
    
    # FormData
    
    class Meta:
        model = CalebModel
        fields = '__all__'
        
class FormData(forms.ModelForm):
    class Meta:
        model = CalebFormModel
        fields = '__all__'