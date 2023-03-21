from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Mission(models.Model):
    nom = models.CharField(max_length=100)
    date_depart = models.DateField()
    lieu_depart = models.CharField(max_length=100)
    date_arrivee = models.DateField()
    lieu_arrivee = models.CharField(max_length=100)
    distance = models.IntegerField()
    autres_charges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    employees = models.ManyToManyField(Employee, blank=True)

    def __str__(self):
        return self.nom
