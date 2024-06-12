from django.contrib import admin

from.models import RoomModel,Topic,Message
# Register your models here.

admin.site.register(RoomModel)
admin.site.register(Topic)
admin.site.register(Message)

