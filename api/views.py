from django.shortcuts import render



from rest_framework.decorators import api_view
from rest_framework.response import Response


from freecodeapp.models import  RoomModel
# from calebform.models import FormModel



from .serializers import RoomSerializer

# # class baseveiw
# from rest_framework.viewsets import ModelViewSet
# # Create your views here.
# from django.views.decorators.csrf import csrf_exempt
# import json



@api_view(['GET'])
def api (request):
    routes =[
        'GET /api'
    ]
    
    return Response(routes)
    
@api_view(['GET'])
def getrooms(request):
    rooms= RoomModel.objects.all()
    serializer = RoomSerializer(rooms,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getroom(request,pk):
    rooms= RoomModel.objects.get(id=pk)
    serializer = RoomSerializer(rooms,many=False)
    return Response(serializer.data)

# @api_view(['POST'])
# def handle_form_submission(request):
#     serializer = RoomSerializer(rooms,many=False)
#     return Response(serializer.data)



