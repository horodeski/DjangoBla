# Generated by Django 4.2.7 on 2023-11-25 01:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_user_telefone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="telefone",
            field=models.IntegerField(blank=True),
        ),
    ]
