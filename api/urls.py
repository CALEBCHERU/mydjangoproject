from django.urls import path, include

# from articleapp.veiws import/ ArticleCreateView
from api import views 




from rest_framework.routers import DefaultRouter
from calebform.urls import calebform_router

from freecodeapp.urls import room_router

router = DefaultRouter()

router.registry.extend(calebform_router.registry)
router.registry.extend(room_router.registry)

urlpatterns = [
    path( 'router/',include(router.urls)),
    
    
    path( 'api/',views.api,name='api'),
    path('api/rooms/',views.getrooms,name='api_rooms'),
    path('api/rooms/<str:pk>/',views.getroom,name='api_room')
    
]

