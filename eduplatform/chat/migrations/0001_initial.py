import django.db.models.deletion
import django.utils.timezone
import mentorship.mixins
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatRoom",
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
                ("name_chat", models.CharField(default="course_name", max_length=100)),
                ("description_topics", models.TextField()),
            ],
            options={
                "verbose_name": "ChatRoom",
                "verbose_name_plural": "ChatRooms",
            },
            bases=(models.Model, mentorship.mixins.DateTimeMixin),
        ),
        migrations.CreateModel(
            name="Message",
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

                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="chat.chatroom"),

                ),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_messages",
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
                "verbose_name": "Message",
                "verbose_name_plural": "Messages",
            },
            bases=(models.Model, mentorship.mixins.DateTimeMixin),
        ),
    ]
