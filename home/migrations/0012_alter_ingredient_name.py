# Generated by Django 4.1.4 on 2023-02-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_alter_category_options_alter_product_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="name",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]