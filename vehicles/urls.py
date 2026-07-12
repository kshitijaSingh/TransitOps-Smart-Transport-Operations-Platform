from django.urls import path
from .views import vehicle_create, vehicle_delete, vehicle_edit, vehicle_list

urlpatterns = [
    path("", vehicle_list, name="vehicle_list"),
    path("new/", vehicle_create, name="vehicle_create"),
    path("<int:pk>/edit/", vehicle_edit, name="vehicle_edit"),
    path("<int:pk>/delete/", vehicle_delete, name="vehicle_delete"),
]
