# Generated by Django 5.0.3 on 2024-03-11 22:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0010_blogpost_views"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]