from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElevatorViewSet, RequestViewSet, ElevatorStatusView

router = DefaultRouter()
router.register(r'elevators', ElevatorViewSet)
router.register(r'requests', RequestViewSet)

urlpatterns = [
    path('status/', ElevatorStatusView.as_view({'get': 'list'}), name='elevator-status'),
    path('', include(router.urls)),
]