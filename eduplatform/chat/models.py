from django.db import models
from django.conf import settings
from mentorship.mixins import DateTimeMixin
from django.utils import timezone

class ChatRoom(models.Model, DateTimeMixin):
    name_chat = models.CharField(max_length=100, default="course_name")
    description_topics = models.TextField()

    def __str__(self):
        return f"{self.pk} - {self.name_chat} "

    class Meta:
        verbose_name = "ChatRoom"
        verbose_name_plural = "ChatRooms"


class Message (models.Model, DateTimeMixin):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    text_message = models.TextField()
    sending_time = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')


    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"{self.text_message} - {self.sending_time} - {self.sender}"   














