# Generated by Django 4.1.2 on 2023-03-27 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "my_trans",
            "0018_alter_employee_first_name_alter_employee_last_name_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="mission",
            name="facture",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="FraisSupplementaire",
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
                ("nom", models.CharField(max_length=255)),
                ("prix", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "mission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_trans.mission",
                    ),
                ),
            ],
        ),
    ]
