# Generated by Django 4.1.4 on 2022-12-16 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("primeira_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cliente",
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
                (
                    "nome",
                    models.CharField(max_length=200, verbose_name="Nome Completo"),
                ),
                (
                    "data_nascimento",
                    models.DateField(
                        blank=True, null=True, verbose_name="Data nascimento"
                    ),
                ),
                (
                    "cpf",
                    models.CharField(
                        blank=True, max_length=11, null=True, verbose_name="CPF"
                    ),
                ),
                (
                    "sexo",
                    models.CharField(
                        choices=[
                            ("M", "Masculino"),
                            ("F", "Feminino"),
                            ("I", "Intersexo"),
                            ("N", "Não declarar"),
                        ],
                        max_length=1,
                        verbose_name="Sexo",
                    ),
                ),
                (
                    "estado_civil",
                    models.CharField(
                        choices=[
                            ("S", "Solteiro"),
                            ("C", "Casado"),
                            ("D", "Divorciado"),
                            ("V", "Viúvo"),
                        ],
                        max_length=1,
                        verbose_name="Estado civil",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
                (
                    "telefone",
                    models.CharField(
                        blank=True,
                        max_length=11,
                        null=True,
                        verbose_name="Nº telefone celular",
                    ),
                ),
            ],
        ),
    ]
