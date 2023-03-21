from django import forms

from my_trans.models import Mission, Employee


class MissionForm(forms.ModelForm):
    employees = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Mission
        fields = [
            'nom',
            'date_depart',
            'lieu_depart',
            'date_arrivee',
            'lieu_arrivee',
            'distance',
            'autres_charges',
            'prix',
            'employees',
        ]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name']
