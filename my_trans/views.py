import json
import logging

from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404

from .forms import MissionForm, EmployeeForm
from .models import Mission, Employee, FraisSupplementaire

logger = logging.getLogger(__name__)

def create_mission(request):

    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            mission = form.save(commit=False)
            mission.save()
            form.save_m2m()  # Maintenant, vous pouvez sauvegarder le champ many to many
            expense_names = request.POST.getlist('expense_name[]')
            expense_prices = request.POST.getlist('expense_price[]')
            for name, price in zip(expense_names, expense_prices):
                frais_supp = FraisSupplementaire(nom=name, prix=price, mission=mission)
                frais_supp.save()
    else:
        form = MissionForm()
    return render(request, 'create_mission.html', {'form': form})


def mission_list(request):
    missions = Mission.objects.all()
    frais_supplementaires = FraisSupplementaire.objects.all()
    return render(request, 'mission_list.html', {'missions': missions, 'frais_supplementaires': frais_supplementaires})
def create_employee(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
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
def edit_mission(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    if request.method == 'POST':
        form = MissionForm(request.POST, instance=mission)
        if form.is_valid():
            form.save()
            return redirect('mission_list')
    else:
        form = MissionForm(instance=mission)
    return render(request, 'edit_mission.html', {'form': form})


def delete_mission(request, mission_id):
    mission = Mission.objects.get(id=mission_id)
    if request.method == 'POST':
        mission.delete()
        return redirect('mission_list')
    return render(request, 'delete_mission.html', {'mission': mission})
