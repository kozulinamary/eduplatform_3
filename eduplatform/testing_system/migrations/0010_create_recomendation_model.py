from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mentorship", "0006_create_model_message"),
        (
            "testing_system",
            "0009_create_add_DateTimeModelMixin_Course_Topic_Article_Test_Question_Answer_models",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Recomendation",
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
                ("text", models.CharField(max_length=100)),
                (
                    "recommended_articles",
                    models.ManyToManyField(blank=True, to="testing_system.article"),
                ),
                (
                    "recommended_courses",
                    models.ManyToManyField(blank=True, to="testing_system.course"),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mentorship.student",
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
                "verbose_name": "recommendation",
                "verbose_name_plural": "recommendations",
            },
        ),
    ]
