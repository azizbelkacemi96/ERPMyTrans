from django.conf.urls.static import static
from django.urls import path

from ERPMyTrans import settings
from . import views

urlpatterns = [
    path("employee_list/", views.employee_list, name="employee_list"),
    path("employee_create/", views.create_employee, name="employee_create"),
    path("create_mission/", views.create_mission, name="create_mission"),
    path("mission_list/", views.mission_list, name="mission_list"),
]
