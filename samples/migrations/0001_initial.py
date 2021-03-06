# Generated by Django 4.0.4 on 2022-04-13 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("grants", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Sample",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("note", models.CharField(blank=True, max_length=255)),
                ("amount", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "grant",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="samples",
                        to="grants.grant",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="samples",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
