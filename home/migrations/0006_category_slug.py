# Generated by Django 4.1.4 on 2023-01-29 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_basket"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(default="", max_length=15),
        ),
    ]