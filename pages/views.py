from django.shortcuts import render,HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("<h1>Hii Caleb</h1>" )

def contact(request):
    return HttpResponse("<h1>Contact</h1>")

def html(request):
    return render(request,"theband.html")
     
     
def base(request):
    my_context={
        "name" : "caleb",
        "Age" : 20,
        "University" : "PIU",
        "list" : [1234,"abc",987,"cheru",20],
        "this_True" : True
    }
    
    return render(request,"base.html", my_context)

def base1(request):
    return render(request,"contact.html")
