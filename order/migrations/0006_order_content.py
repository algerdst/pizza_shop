# Generated by Django 4.1.4 on 2023-02-20 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0014_alter_category_options_alter_product_options"),
        ("order", "0005_order_payment"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="content",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="home.basket",
            ),
        ),
    ]