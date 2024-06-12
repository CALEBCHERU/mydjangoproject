from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse




from django.views.generic import View
from.form import RoomForm
from .models import RoomModel,Topic

from django.db.models import Q

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .models import Message

# api
from .serializers import  RoomSerializer
from rest_framework.viewsets import ModelViewSet

#connects the api to the model and serializer
class RoomSet(ModelViewSet):
    queryset =  RoomModel.objects.all()
    serializer_class = RoomSerializer
    



# Create your views here.


def loginpage(request):
    page = "login"
    
    
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error( request, "Username doesn't exist." )
        
        user = authenticate(request,username=username,password=password)
        
        # check if the input is empty or the user or pass exist
        
        if (user is not None):
            # adds session soas toremain login in
            login(request, user )
            return redirect('home_room')
        
        else:
            messages.error(request, "Username and Password doesn't exist." )
            
            
        
            
    
    context= {'page':page}
    return render (request ,"login_reg.html",context)

def registerpage(request):
    page = "register"
    form = UserCreationForm()
    
    if request.method == 'POST':
        # the below code is used to retrive the data from the user
        form = UserCreationForm(request.POST )
        if form.is_valid():
            user = form.save( commit=False )
            user.username= user.username.lower()
            user.save()
            return redirect( 'home_room' )
        else:
            messages.error(request, "Username and Password doesn't exist." )
            
            
    
    context ={'page':page, 'form':form}
    return render(request,"login_reg.html",context)

def logoutuser(request):
    
    logout(request)
    return render(request,'logoutuser.html')

def freecode(request):

    q = request.GET.get('q') if request.GET.get('q') else ""
    
    # (icontains is a case-insensitive containment test).
    rooms = RoomModel.objects.filter(
        Q(topic__name__icontains=q)|
        Q(host__username__icontains=q)|
        Q(description__icontains=q)
        )
    
    topics = Topic.objects.all()
    
    messages = Message.objects.all().order_by('-created') 
    Message_count = Message.objects.count()
    
    
    
    # if request.method == 'POST':
    #     userc = request.user
    #     room = get_object_or_404(RoomModel, id=pk)
    #     messagessc = Message.objects.created(
    #         user = userc
    #         room = room
    #         body = request.POST.get('body') 
    #     )
    
    room_count = rooms.count()
    
    context = {"object": rooms, "topics": topics, "q": q,'room_count':room_count, 'messages': messages, 'Message_count': Message_count}
    
    return render(request, "freecode.html", context)

    
class BaseView(View):
    template_names = "BaseView_View.html"
    
    def get(self,request):
        return render(request,self.template_names)
    

@login_required(login_url='login_room')
def Room_create(request):
    form = RoomForm
    context = {'form':form}
    
    # this code prints on the server terminal
    if request.method == 'POST':
        # print(request.method)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_room')
        
        
    
    
    return render(request,"RoomForm.html",context)

def Room_list(request):
    querryset = RoomModel.objects.all()
    context = {"object":querryset}
    
    return render(request,"RoomLIst.html",context)

@login_required(login_url='login_room')
def Room_update(request,pk):
    # room = get_object_or_404(RoomModel, id=id)
    querryset = RoomModel.objects.all()
    room = RoomModel.objects.get(id=pk)
    
    # from django.http import HttpResponse
    # this helps us to write a message without having to create a html file
      
    if request.user != room.host:
        return HttpResponse( "<h1> You don't have the permission to edit this user<h1> " )
    
    
    
    
    # returns all the data of that room
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        
        # def clean_data(self,ArticleForm):
        # print(ArticleForm.cleaned_data)
        # return super().form_valid(ArticleForm)
     
        if form.is_valid():
            # print(RoomForm.cleaned_data)
            form.save()
            return redirect('list_room')
    else:
        form = RoomForm(instance=room)
    
    context = {"object":querryset,'form': form}
    # context = {"object":querryset}
    return render(request, "RoomForm.html", context)

@login_required(login_url='login_room')
def Room_delete(request,pk):
    
    # room = get_object_or_404(RoomModel, id=id)
    querryset = RoomModel.objects.all()
    context = {"object":querryset}
    room = RoomModel.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse( "<h1> You don't have the permission to delete this user<h1> " )
    
    
    
  
    
    if request.method == 'POST':
        # returns all the data of that room
        room.delete()
        return redirect('list_room')
        
       
    

    return render(request, "deleteroom.html", context)


def messages_v(request, pk):
    room = get_object_or_404(RoomModel, id=pk)
    messages = room.message_set.all()
    context = { 'messages': messages }
    return render(request, 'message.html', context)

def messages_all(request):
    messages = Message.objects.all().order_by('-created') 
    context = { 'messages': messages }
    
    if request.method == 'POST':
        messagec = Message.objects.create(
            message=request.POST.get('message'),
            user=request.user,
            
        )
    
    
    return render(request, 'message.html', context)
