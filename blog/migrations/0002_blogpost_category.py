# Generated by Django 5.0.3 on 2024-03-07 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="category",
            field=models.CharField(default="General", max_length=100),
        ),
    ]
