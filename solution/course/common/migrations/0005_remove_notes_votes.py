# Generated by Django 4.2.7 on 2024-02-24 13:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0004_remove_notes_user_votes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notes",
            name="votes",
        ),
    ]