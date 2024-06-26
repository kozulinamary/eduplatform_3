import django.db.models.deletion
import mentorship.mixins
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mentorship", "0002_create_teacher_model"),

    ]

    operations = [
        migrations.AlterModelManagers(

            name="user",
            managers=[],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("rating", models.DecimalField(decimal_places=2, max_digits=4)),
                ("age", models.IntegerField()),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "student",
                "verbose_name_plural": "students",

            },
            bases=(models.Model, mentorship.mixins.DateTimeMixin),
        ),
    ]
