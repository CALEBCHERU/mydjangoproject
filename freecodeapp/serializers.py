from rest_framework.serializers import ModelSerializer
from .models import RoomModel

#it like a form
#the serializer reads the contents in the model and passes it to the api
class RoomSerializer(ModelSerializer):
    class Meta:
        model = RoomModel
        fields = ('id','room_name','description','host','topic')
        # fields = ('id','name','email')