# elevator-problem
Elevator system assignment - Jumping Minds


The Elevator System Project is a Django-based application that simulates an elevator system capable of handling multiple elevators and their operations. This project provides a RESTful API for managing elevators, assigning requests, and fetching elevator status.


Installation : 
1. Clone the repository or download the project source code.
2. Install the required Python packages using pip.

    pip install -r requirements.txt


Setup and Configuration :
1. Navigate to the project root directory.
2. Perform database migrations to create the necessary tables.

    python manage.py makemigrations
    python manage.py migrate


Create a superuser to access the Django admin interface

    python manage.py createsuperuser


Start the Django development server.

    python manage.py runserver


Usage
The Elevator System Project offers multiple APIs for managing the elevators and their requests.

Initialize Elevator System
Endpoint: /elevators/
Method: POST
Request Body: JSON payload with num_elevators to initialize the elevator system with a given number of elevators.
    curl -X POST http://localhost:8000/elevators/ -H "Content-Type: application/json" -d '{"num_elevators": 5}'


Submit User Request
Endpoint: /requests/
Method: POST
Request Body: JSON payload with floor and direction for user request.
    curl -X POST http://localhost:8000/requests/ -H "Content-Type: application/json" -d '{"floor": 7"direction":"up"}'



Fetch Elevator Status
Endpoint: /status/
Method: GET
curl -X GET http://localhost:8000/status/



Fetch All Elevators
Endpoint: /elevators/
Method: GET
curl -X GET http://localhost:8000/elevators/



Fetch All Requests
Endpoint: /requests/
Method: GET
curl -X GET http://localhost:8000/requests/


Note : Please use Django Admin interface to add elevators to database