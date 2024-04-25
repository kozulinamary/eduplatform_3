import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mentorship", "0004_create_group_model"),
        ("testing_system", "0003_create_topic_model"),

    ]

    operations = [
        migrations.CreateModel(

            name="Article",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("teacher", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="mentorship.teacher")),
                ("topic", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="testing_system.topic")),
            ],
            options={
                "verbose_name": "article",
                "verbose_name_plural": "articles",

            },
        ),
    ]
