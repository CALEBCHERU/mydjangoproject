from django.shortcuts import render,redirect

from calebform.models import CalebModel,CalebFormModel  
from calebform.calebform import CalebForm



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# class baseveiw api
from calebform.serializers import  CalebFormSerializer
from rest_framework.viewsets import ModelViewSet

#connects the api to the model and serializer
class CalebFormSet(ModelViewSet):
    queryset =  CalebFormModel.objects.all()
    serializer_class = CalebFormSerializer
    



# Create your views here.

def create(request):
    my_form = CalebForm
    
    
    # if request.method == 'POST':
    #     my_form = CalebForm( request.POST )
    #     if my_form.is_valid:
    #         my_form.save()
    #         return redirect('form')
    #     else:
    #          print(form.errors)
     
    if request.method == "POST":
        my_form = CalebForm(request.POST)
        if my_form.is_valid():
            #my data is good
            print(my_form.cleaned_data)
            CalebModel.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
            
    context = {'form': my_form}

    return render(request, 'form.html', context)

def update(request):
    pass

# @csrf_exempt  # This disables CSRF protection for this view
# def handle_form_submission(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         print(data)
        
#         # Process your data here
#         # For example, you could save it to the database
#         form_data = CalebFormModel.objects.create(
#             name = data['name' ],
#             email =data['email'],
#             # Save other fields as needed
#         )
#         return JsonResponse({'message': 'Form data received successfully'})
#     return JsonResponse({'error': 'Invalid request'}, status=400)


def createformadata(request):
    pass
    # my_form = FormModel
    
            
    # context = {'form':my_form}

    # return render(request, 'form.html', context)
