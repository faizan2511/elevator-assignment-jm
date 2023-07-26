from django.contrib import admin
from .models import Elevator, Request

# Register your models here.

class ElevatorAdmin(admin.ModelAdmin) :
    list_display = ['status', 'current_floor', 'is_moving_up', 'is_moving_down', 'is_door_open']

class RequestAdmin(admin.ModelAdmin) :
    list_display = ['elevator', 'floor', 'direction']

admin.site.register(Elevator, ElevatorAdmin)
admin.site.register(Request, RequestAdmin)
