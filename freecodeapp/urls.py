from django.urls import path

# from articleapp.veiws import ArticleCreateView
from freecodeapp import views



# api
from .views import RoomSet
from rest_framework.routers import DefaultRouter

room_router = DefaultRouter()

room_router.register('roomrouter', RoomSet)




# app_name= "room"

urlpatterns = [
    
    path('roomlogin/',views.loginpage,name="login_room" ),
    path('roomreg/',views.registerpage,name="register_room" ),
    path('roomlogout/',views.logoutuser,name="logout_room" ),
    
    
    path('room/',views.freecode,name="home_room"),
    path('room/create/', views.Room_create, name='create_room'),
    path('room/list/', views.Room_list, name='list_room'),
    path('room/update/<str:pk>/', views.Room_update, name='update_room'),
    path('room/delete/<str:pk>/ ', views.Room_delete, name='delete_room'),
    
    path('room/messages/<int:pk>/', views.messages_v , name='messsages_room'),
     path('room/messages/', views.messages_all, name='all-messages')

]
