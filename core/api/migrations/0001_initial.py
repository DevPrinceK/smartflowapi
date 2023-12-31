# Generated by Django 4.2.4 on 2023-08-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Humidity",
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
                ("humidity", models.IntegerField()),
                ("date", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Moisture",
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
                ("moisture", models.IntegerField()),
                ("date", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Temperature",
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
                ("temperature", models.DecimalField(decimal_places=2, max_digits=5)),
                ("date", models.CharField(max_length=100)),
            ],
        ),
    ]
