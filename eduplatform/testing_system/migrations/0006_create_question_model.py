import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("testing_system", "0005_create_test_model"),

    ]

    operations = [
        migrations.CreateModel(

            name="Question",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.CharField(max_length=100)),
                ("is_important", models.BooleanField(default=False)),
                ("test", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="testing_system.test")),
            ],
            options={
                "verbose_name": "guestion",
                "verbose_name_plural": "guestions",

            },
        ),
    ]
