from django.shortcuts import render,HttpResponse

from .forms import RawProduct

from .models import product

from django.views.generic import *

# Create your views here.
def baseProduct(request):
    return render (request,"baseproduct.html" )


def RawProduct_v(request):
    my_form = RawProduct()
    if request.method == "POST":
        my_form = RawProduct(request.POST)
        if my_form.is_valid():
            #my data is good
            print(my_form.cleaned_data)
            product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form" : my_form
        
    }
    return render (request,"product/product_form.html", context)

#Acess indormation from database
def dynamic_lookup(request, my_id):
    obj = product.objects.get(id=my_id)
    
    context ={
        "object": obj
    }
    
    return render(request,"product/productdetail.html", context)

#this is a class based View
class ProductListView(ListView):
    template_name='product/product_list.html'
    queryset = product.objects.all()
    
    
# class ModelNameList(ListView):
#     model = ModelName
#     context_object_name = ''
#     template_name='



