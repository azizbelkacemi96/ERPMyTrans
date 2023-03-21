from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Mission(models.Model):
    name = models.CharField(max_length=100, default=None)
    departure_location = models.CharField(max_length=100, default=None, null=True)
    departure_date = models.DateField(default=None, null=True)
    arrival_location = models.CharField(max_length=100, default=None, null=True)
    arrival_date = models.DateField(default=None, null=True)
    km_travelled = models.PositiveIntegerField(default=None, null=True)
    employees = models.ManyToManyField(Employee)
    extra_charges = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
