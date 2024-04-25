import mentorship.mixins
from django.db import migrations, models



class Migration(migrations.Migration):
    dependencies = [
        ("mentorship", "0004_create_group_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="SiteUser",
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
                ("username", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=128)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_blocked", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Site user",
                "verbose_name_plural": "Site users",
            },
            bases=(models.Model, mentorship.mixins.DateTimeMixin),
        ),
    ]
