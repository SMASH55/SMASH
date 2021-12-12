from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Restaurant",
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
                ("name", models.CharField(default="", max_length=200)),
                ("name_of_restaurant", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200, unique=True)),
                (
                    "phone",
                    models.CharField(
                        max_length=10,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
                ("address", models.CharField(max_length=200)),
                ("verified", models.BooleanField(default=False)),
                ("is_res", models.BooleanField(default=False)),
                (
                    "about",
                    models.TextField(default="Add a description here!", max_length=500),
                ),
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/profile/"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rest",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("pic", models.ImageField(blank=True, null=True, upload_to="images/")),
                ("body", models.TextField()),
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
            name="FoodRedistributor",
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
                ("name", models.CharField(default="", max_length=200)),
                ("name_of_food_redis", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200, unique=True)),
                (
                    "phone",
                    models.CharField(
                        max_length=10,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
                ("address", models.CharField(max_length=200)),
                ("verified", models.BooleanField(default=False)),
                ("is_food_redis", models.BooleanField(default=False)),
                (
                    "about",
                    models.TextField(default="Add a description here!", max_length=500),
                ),
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/profile/"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="foodredis",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
