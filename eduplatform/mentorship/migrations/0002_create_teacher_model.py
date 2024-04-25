import django.db.models.deletion
import mentorship.mixins
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mentorship", "0001_create_user_model"),
    ]

    operations = [
        migrations.CreateModel(

            name="Teacher",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("experience", models.IntegerField()),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "teacher",
                "verbose_name_plural": "teachers",

            },
            bases=(models.Model, mentorship.mixins.DateTimeMixin),
        ),
    ]
