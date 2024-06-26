import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mentorship", "0004_create_group_model"),
        ("testing_system", "0007_create_answer_model"),

    ]

    operations = [
        migrations.CreateModel(

            name="Attempt",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("score", models.PositiveSmallIntegerField(default=0)),
                ("student", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="mentorship.student")),
                ("test", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="testing_system.test")),
            ],
            options={
                "verbose_name": "attempt",
                "verbose_name_plural": "attempts",

            },
        ),
    ]
