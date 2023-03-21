# views.py
import logging

from django.shortcuts import render, redirect
from django.forms import formset_factory
from .forms import MissionForm
from .models import Mission, Employee

logger = logging.getLogger(__name__)

def create_mission(request):
    EmployeeFormSet = formset_factory(MissionForm, extra=1)
    if request.method == "POST":
        mission_form = MissionForm(request.POST)
        formset = EmployeeFormSet(request.POST)
        if mission_form.is_valid() and formset.is_valid():
            mission = mission_form.save()
            employees = formset.cleaned_data
            for employee in employees:
                if employee:
                    full_name = employee['first_name'] + ' ' + employee['last_name']
                    employee = employees[0]
                    print(employee)
                    emp = Employee.objects.get(first_name=employee['first_name'], last_name=employee['last_name'])
                    print(emp)
                    mission.employees.add(emp)
    else:
        mission_form = MissionForm()
        formset = EmployeeFormSet()
    context = {
        "mission_form": mission_form,
        "formset": formset,
    }
    return render(request, "create_mission.html", context)




def mission_list(request):
    missions = Mission.objects.all()
    context = {
        "missions": missions,
    }
    return render(request, "mission_list.html", context)


def create_employee(request):
    form = MissionForm()
    if request.method == "POST":
        form = MissionForm(request.POST)
        if form.is_valid():
            form.save()
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
