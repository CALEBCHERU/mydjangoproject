from rest_framework.serializers import ModelSerializer
from .models import CalebFormModel

#it like a form
#the serializer reads the contents in the model and passes it to the api
class CalebFormSerializer(ModelSerializer):
    class Meta:
        model = CalebFormModel
        fields = ('id','name','email')
