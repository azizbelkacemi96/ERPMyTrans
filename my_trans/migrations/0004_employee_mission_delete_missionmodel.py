# Generated by Django 4.1.6 on 2023-03-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_trans", "0003_missionmodel_delete_demenagement_delete_employee"),
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
            ],
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
                ("name", models.CharField(max_length=100)),
                ("departure_location", models.CharField(max_length=100)),
                ("departure_date", models.DateField()),
                ("arrival_location", models.CharField(max_length=100)),
                ("arrival_date", models.DateField()),
                ("km_travelled", models.PositiveIntegerField()),
                ("extra_charges", models.TextField(blank=True)),
                ("employees", models.ManyToManyField(to="my_trans.employee")),
            ],
        ),
        migrations.DeleteModel(
            name="MissionModel",
        ),
    ]