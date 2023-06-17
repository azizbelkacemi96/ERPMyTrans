from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Mission(models.Model):
    facture = models.BooleanField(default=False)
    nom = models.CharField(max_length=100)
    date_depart = models.DateField()
    lieu_depart = models.CharField(max_length=100)
    date_arrivee = models.DateField()
    lieu_arrivee = models.CharField(max_length=100)
    distance = models.IntegerField()
    autres_charges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    employees = models.ManyToManyField(Employee, blank=True)
    lieu_depart = models.CharField(max_length=255)
    lieu_arrivee = models.CharField(max_length=255)
    hotel = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    volume = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    CATEGORIES = [
        ('moving', 'Moving'),
        ('cocolis', 'Cocolis'),
        ('categorie1', 'Categorie1'),
        ('categorie2', 'Categorie2'),
        ('categorie3', 'Categorie3'),
        ('extrat', 'Extrat'),
        ('fret', 'Fret'),
        ('particulier', 'Particulier'),
        ('odd', 'Odd'),
    ]
    categorie = models.CharField(max_length=50, choices=CATEGORIES, default='moving')
    peage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    location = models.DecimalField(max_digits=10, decimal_places=2, default=0)
class FraisSupplementaire(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nom} ({self.prix})"