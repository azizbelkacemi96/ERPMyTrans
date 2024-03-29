# Generated by Django 4.1.6 on 2023-03-06 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_trans", "0009_alter_mission_departure_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mission",
            name="arrival_date",
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name="mission",
            name="arrival_location",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name="mission",
            name="departure_location",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name="mission",
            name="km_travelled",
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name="mission",
            name="name",
            field=models.CharField(default=None, max_length=100),
        ),
    ]
