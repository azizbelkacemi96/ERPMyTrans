from django import forms

from my_trans.models import Mission, Employee


class MissionForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    start_location = forms.CharField(max_length=100)
    start_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))
    end_location = forms.CharField(max_length=100)
    end_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))
    km_travelled = forms.IntegerField()
    employees = forms.ModelMultipleChoiceField(queryset=Employee.objects.all(),
                                               widget=forms.SelectMultiple(attrs={"class": "my-custom-class"}))

    class Meta:
        model = Mission
        fields = [
            "name",
            "start_location",
            "start_date",
            "start_time",
            "end_location",
            "end_date",
            "end_time",
            "km_travelled",
            "employees",
        ]

    def clean_departure_date(self):
        departure_date = self.cleaned_data.get("departure_date")
        if not departure_date:
            raise forms.ValidationError("La date de départ est obligatoire.")
        return departure_date
