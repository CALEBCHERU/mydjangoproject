from django.urls import path
from .views import create 
# handle_form_submission

from .views import CalebFormSet
from rest_framework.routers import DefaultRouter

calebform_router = DefaultRouter()

calebform_router.register('calebform', CalebFormSet)

# name = "caleb"

urlpatterns = [
    path('caleb/form/', create,name="form_caleb"),
    # path('submit-form/', handle_form_submission, name='submit_form'),
]

