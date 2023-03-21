# views.py
import logging

from django.shortcuts import render, redirect
from django.forms import formset_factory
from .forms import MissionForm, EmployeeForm
from .models import Mission, Employee

logger = logging.getLogger(__name__)

def create_mission(request):
    if request.method == "POST":
        mission_form = MissionForm(request.POST)
        if mission_form.is_valid():
            mission = mission_form.save()
            #return redirect('mission_list')  # Redirige vers la liste des missions après avoir créé une mission
    else:
        mission_form = MissionForm()
    context = {
        "mission_form": mission_form,
    }
    return render(request, "create_mission.html", context)





def mission_list(request):
    missions = Mission.objects.all()
    context = {
        "missions": missions,
    }
    return render(request, "mission_list.html", context)



def create_employee(request):
    form = EmployeeForm()  # Utilisez EmployeeForm au lieu de MissionForm
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
           # return redirect('employee_list')  # Redirigez vers la liste des employés après avoir créé un employé
    context = {
        "form": form,
    }
    return render(request, "create_employee.html", context)


def employee_list(request):
    employees = Employee.objects.all()
    context = {
        "employees": employees,
    }
    return render(request, "employee_list.html", context)