from django.db import migrations, models
import django.db.models.deletion
import mentorship.mixins


class Migration(migrations.Migration):
    dependencies = [
        ("mentorship", "0006_create_model_message"),
        ("testing_system", "0011_create_recommendation_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestAccess",
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
                    "shared_with_teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shared_tests",
                        to="mentorship.teacher",
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="testing_system.test",
                    ),
                ),
            ],
            options={
                "verbose_name": "share with teacher",
                "verbose_name_plural": "share with teachers",
            },
            bases=(models.Model, mentorship.mixins.DateTimeMixin),
        ),
    ]
