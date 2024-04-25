import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mentorship", "0004_create_group_model"),
        ("testing_system", "0001_create_group_model"),

    ]

    operations = [
        migrations.AlterModelOptions(

            name="course",
            options={"verbose_name": "course", "verbose_name_plural": "courses"},
        ),
        migrations.AddField(
            model_name="course",
            name="name",
            field=models.CharField(default="course_name", max_length=100),
        ),
        migrations.AddField(
            model_name="course",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name="course",
            name="teacher",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="mentorship.teacher"),

        ),
    ]
