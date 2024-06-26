import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("testing_system", "0002_create_course_model_testing_system"),

    ]

    operations = [
        migrations.CreateModel(

            name="Topic",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("course", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="testing_system.course")),
            ],
            options={
                "verbose_name": "topic",
                "verbose_name_plural": "topics",

            },
        ),
    ]
