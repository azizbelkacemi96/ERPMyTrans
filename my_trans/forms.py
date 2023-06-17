from django import forms
from my_trans.models import Mission, Employee, FraisSupplementaire

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
            'hotel',
            'volume',
            'categorie',
            'peage',
            'location',
        ]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name']
    def __str__(self):
        if self.last_name:
            return self.first_name + " " + self.last_name
        else:
            return self.first_name