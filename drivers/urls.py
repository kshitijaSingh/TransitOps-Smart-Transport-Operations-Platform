from django.urls import path
from .views import driver_create, driver_delete, driver_edit, driver_list

urlpatterns = [
    path("", driver_list, name="driver_list"),
    path("new/", driver_create, name="driver_create"),
    path("<int:pk>/edit/", driver_edit, name="driver_edit"),
    path("<int:pk>/delete/", driver_delete, name="driver_delete"),
]
