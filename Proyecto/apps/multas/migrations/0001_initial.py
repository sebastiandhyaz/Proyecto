# Generated by Django 5.2.2 on 2025-06-14 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("prestamos", "0001_initial"),
        ("socios", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Multa",
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
                ("monto", models.DecimalField(decimal_places=2, max_digits=8)),
                ("motivo", models.CharField(max_length=255)),
                ("fecha_generada", models.DateField(auto_now_add=True)),
                ("pagada", models.BooleanField(default=False)),
                ("fecha_pago", models.DateField(blank=True, null=True)),
                ("anulada", models.BooleanField(default=False)),
                ("justificacion_anulacion", models.TextField(blank=True)),
                (
                    "prestamo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="multas",
                        to="prestamos.prestamo",
                    ),
                ),
                (
                    "socio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="multas",
                        to="socios.socio",
                    ),
                ),
            ],
        ),
    ]
