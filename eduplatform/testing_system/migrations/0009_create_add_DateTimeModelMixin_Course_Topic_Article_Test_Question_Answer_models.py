from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("testing_system", "0008_create_attempt_model"),

    ]

    operations = [
        migrations.AlterModelOptions(

            name="question",
            options={"verbose_name": "question", "verbose_name_plural": "questions"},

        ),
    ]
