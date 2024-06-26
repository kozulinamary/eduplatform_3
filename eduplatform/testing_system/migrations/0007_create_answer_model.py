import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("testing_system", "0006_create_question_model"),

    ]

    operations = [
        migrations.CreateModel(

            name="Answer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.CharField(max_length=100)),
                ("is_correct", models.BooleanField(default=False)),
                ("question", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="testing_system.question")),
            ],
            options={
                "verbose_name": "answer",
                "verbose_name_plural": "answers",

            },
        ),
    ]
