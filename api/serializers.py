from rest_framework.serializers import ModelSerializer
from freecodeapp.models import RoomModel


class RoomSerializer(ModelSerializer):
    class Meta:
        model = RoomModel
        fields = '__all__'
        
