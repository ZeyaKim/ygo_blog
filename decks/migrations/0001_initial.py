# Generated by Django 5.0.3 on 2024-03-13 20:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Deck",
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
                ("deck_name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="DeckPost",
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
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("deck_img", models.ImageField(upload_to="decks/images/")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeckInDeckPost",
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
                    "deck_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="decks.deck"
                    ),
                ),
                (
                    "deck_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="decks.deckpost"
                    ),
                ),
            ],
        ),
    ]
