# Generated by Django 4.1.4 on 2023-02-03 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_is_verificated_emailverification"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="is_verificated",
            new_name="is_verified",
        ),
    ]