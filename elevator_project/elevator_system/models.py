from django.db import models
# Create your models here.

class Elevator(models.Model) :
    OPERATIONAL = 'Operational'
    MAINTENANCE = 'Maintenance'

    STATUS_CHOICES = [(OPERATIONAL, 'Operational'), (MAINTENANCE, 'Maintenance')]

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=OPERATIONAL)
    current_floor = models.IntegerField(default=1)
    is_moving_up = models.BooleanField(default=False)
    is_moving_down = models.BooleanField(default=False)
    is_door_open = models.BooleanField(default=False)

    def __str__(self) :
        return f"Elevator {self.pk} - {self.status}"
    

class Request(models.Model) :
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE, related_name='requests')
    floor = models.IntegerField()
    direction = models.CharField(max_length=5)

    def __str__(self):
        return f'Request: Elevator {self.elevator_id}, Floor {self.floor}, Direction {self.direction}'

