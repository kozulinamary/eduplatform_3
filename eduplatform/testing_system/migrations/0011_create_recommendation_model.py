from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mentorship", "0006_create_model_message"),
        ("testing_system", "0010_create_recomendation_model"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Recomendation",
            new_name="Recommendation",
        ),
    ]
