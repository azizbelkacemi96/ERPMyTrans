# Generated by Django 4.1.2 on 2023-03-21 19:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_trans", "0017_delete_mission"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="first_name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="employee",
            name="last_name",
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.CreateModel(
            name="Mission",
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
                ("date_depart", models.DateField()),
                ("lieu_depart", models.CharField(max_length=100)),
                ("date_arrivee", models.DateField()),
                ("lieu_arrivee", models.CharField(max_length=100)),
                ("distance", models.IntegerField()),
                (
                    "autres_charges",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "prix",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "employees",
                    models.ManyToManyField(blank=True, to="my_trans.employee"),
                ),
            ],
        ),
    ]
