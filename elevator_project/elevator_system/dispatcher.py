class ElevatorSystem:
    def __init__(self, num_elevators):
        self.elevators = [Elevator() for _ in range(num_elevators)]

    def assign_elevator(self, floor, direction):
        # Find the elevator that is most optimal for the user's request
        optimal_elevator = None
        min_distance = float('inf')

        for elevator in self.elevators:
            if elevator.status == Elevator.OPERATIONAL:
                distance = abs(elevator.current_floor - floor)
                if distance < min_distance:
                    optimal_elevator = elevator
                    min_distance = distance

        if optimal_elevator is not None:
            optimal_elevator.add_request(floor, direction)
            return optimal_elevator
        else:
            return None

class Elevator:
    OPERATIONAL = 'Operational'
    MAINTENANCE = 'Maintenance'

    STATUS_CHOICES = [
        (OPERATIONAL, 'Operational'),
        (MAINTENANCE, 'Maintenance'),
    ]

    def __init__(self):
        self.status = Elevator.OPERATIONAL
        self.current_floor = 1
        self.is_moving_up = False
        self.is_moving_down = False
        self.is_door_open = False
        self.requests = []

    def __str__(self):
        return f'Elevator - {self.status}'

    def add_request(self, floor, direction):
        self.requests.append({'floor': floor, 'direction': direction})
        self.process_requests()

    def process_requests(self):
        if not self.is_moving_up and not self.is_moving_down:
            if self.requests:
                next_floor = self.requests[0]['floor']
                if next_floor > self.current_floor:
                    self.is_moving_up = True
                elif next_floor < self.current_floor:
                    self.is_moving_down = True
                else:
                    self.open_door()

    def open_door(self):
        self.is_door_open = True
        # Simulate door opening delay
        self.is_door_open = False
        self.remove_completed_requests()

    def remove_completed_requests(self):
        completed_requests = [request for request in self.requests if request['floor'] == self.current_floor]
        for request in completed_requests:
            self.requests.remove(request)

        if not self.requests:
            self.is_moving_up = False
            self.is_moving_down = False

    def move_up(self):
        self.current_floor += 1
        self.remove_completed_requests()

    def move_down(self):
        self.current_floor -= 1
        self.remove_completed_requests()

    def stop(self):
        self.is_moving_up = False
        self.is_moving_down = False

    def set_maintenance(self):
        self.status = Elevator.MAINTENANCE

    def set_operational(self):
        self.status = Elevator.OPERATIONAL