# Generated by Django 4.1.4 on 2022-12-20 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("primeira_app", "0002_cliente"),
    ]

    operations = [
        migrations.CreateModel(
            name="Endereco",
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
                    "rua",
                    models.CharField(max_length=200, null=True, verbose_name="Rua"),
                ),
                ("numero", models.IntegerField(null=True, verbose_name="Número")),
                (
                    "bairro",
                    models.CharField(max_length=100, null=True, verbose_name="Bairro"),
                ),
                (
                    "cidade",
                    models.CharField(max_length=50, null=True, verbose_name="Cidade"),
                ),
                (
                    "estado",
                    models.CharField(max_length=100, null=True, verbose_name="Estado"),
                ),
                ("cep", models.IntegerField(null=True, verbose_name="CEP")),
                (
                    "pais",
                    models.CharField(max_length=50, null=True, verbose_name="Cidade"),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="autor",
            options={"verbose_name_plural": "Autores"},
        ),
        migrations.AlterModelOptions(
            name="livro",
            options={"verbose_name_plural": "Livros"},
        ),
        migrations.AlterField(
            model_name="cliente",
            name="cpf",
            field=models.CharField(max_length=120, null=True, verbose_name="CPF"),
        ),
        migrations.AddField(
            model_name="cliente",
            name="endereco",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="primeira_app.endereco",
                verbose_name="Endereco",
            ),
        ),
    ]
