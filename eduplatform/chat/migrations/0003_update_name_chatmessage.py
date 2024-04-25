from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mentorship.mixins


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0002_add_user_to_chatroom"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text_message", models.TextField()),
                (
                    "sending_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "chatroom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="chat.chatroom"
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_chatmessage",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "ChatMessage",
                "verbose_name_plural": "ChatMessage",
            },
            bases=(models.Model, mentorship.mixins.DateTimeMixin),
        ),
        migrations.DeleteModel(
            name="Message",
        ),
    ]
