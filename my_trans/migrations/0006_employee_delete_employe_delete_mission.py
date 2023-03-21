# Generated by Django 4.1.6 on 2023-03-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_trans", "0005_employe_rename_arrival_date_mission_date_arrivee_and_more"),
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=15)),
                ("address", models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name="Employe",
        ),
        migrations.DeleteModel(
            name="Mission",
        ),
    ]
