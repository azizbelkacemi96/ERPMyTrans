# Generated by Django 4.1.6 on 2023-03-03 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_trans", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100)),
                ("prenom", models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name="demenagement",
            name="cout",
        ),
        migrations.RemoveField(
            model_name="demenagement",
            name="date_arrivee",
        ),
        migrations.RemoveField(
            model_name="demenagement",
            name="date_depart",
        ),
        migrations.RemoveField(
            model_name="demenagement",
            name="metres_cube",
        ),
        migrations.AddField(
            model_name="demenagement",
            name="date",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="demenagement",
            name="distance",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="demenagement",
            name="lieu_arrivee",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="demenagement",
            name="lieu_depart",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="demenagement",
            name="nb_metres_cube",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="demenagement",
            name="nom",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="demenagement",
            name="employes",
            field=models.ManyToManyField(to="my_trans.employee"),
        ),
    ]
