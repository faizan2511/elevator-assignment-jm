from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Elevator, Request
from .serializers import ElevatorSerializer, RequestSerializer
from .dispatcher import ElevatorSystem


class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    def create(self, request):
        num_elevators = int(request.data.get('num_elevators', 1))
        elevator_system = ElevatorSystem(num_elevators)
        return Response({'message': f'{num_elevators} elevators have been created.'}, status=status.HTTP_201_CREATED)


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def create(self, request):
        floor = request.data.get('floor')
        direction = request.data.get('direction')

        if floor is None or direction not in ['up', 'down']:
            return Response({'error': 'Invalid request data.'}, status=status.HTTP_400_BAD_REQUEST)

        elevator_system = ElevatorSystem()
        elevator = elevator_system.assign_elevator(floor, direction)

        if elevator:
            return Response({'message': f'Elevator {elevator.pk} has been assigned to floor {floor}.'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No available elevators at the moment. Please wait.'},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)

class ElevatorStatusView(viewsets.ViewSet):
    def list(self, request):
        elevators = Elevator.objects.all()
        serializer = ElevatorSerializer(elevators, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
