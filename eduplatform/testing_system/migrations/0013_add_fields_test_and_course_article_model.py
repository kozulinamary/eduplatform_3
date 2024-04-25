from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("testing_system", "0012_create_test_access_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="course",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="testing_system.course",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="test",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="testing_system.test",
            ),
        ),
    ]
