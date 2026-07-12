from django.urls import include, path
from rest_framework.routers import DefaultRouter

from vehicles.api import VehicleViewSet
from drivers.api import DriverViewSet
from trips.api import TripViewSet
from maintenance.api import MaintenanceViewSet
from expenses.api import ExpenseViewSet
from reports.api import ReportViewSet

router = DefaultRouter()
router.register(r"vehicles", VehicleViewSet, basename="vehicle")
router.register(r"drivers", DriverViewSet, basename="driver")
router.register(r"trips", TripViewSet, basename="trip")
router.register(r"maintenance", MaintenanceViewSet, basename="maintenance")
router.register(r"expenses", ExpenseViewSet, basename="expense")
router.register(r"reports", ReportViewSet, basename="report")

urlpatterns = [
    path("", include(router.urls)),
]
