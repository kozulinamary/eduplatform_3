from django.conf import settings
from django.db import models
from django.utils import timezone
from mentorship.mixins import DateTimeMixin
from mentorship.models import User



class ChatRoom(models.Model, DateTimeMixin):
    name_chat = models.CharField(max_length=100, default="course_name")
    description_topics = models.TextField()

    participant = models.ManyToManyField(User, blank=True)

    def get_participant_count(self):
        if self.participant.exists():
            return self.participant.count()
        else:
            return 0

    def join(self, user):
        if user not in self.participant.all():
            self.participant.add(user)

    def leave(self, user):
        if user in self.participant.all():
            self.participant.remove(user)

    def __str__(self):
        return f"{self.pk} - {self.name_chat} - {', '.join(str(participant) for participant in self.participant.all())}"


    class Meta:
        verbose_name = "ChatRoom"
        verbose_name_plural = "ChatRooms"



class ChatMessage(models.Model, DateTimeMixin):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    text_message = models.TextField()
    sending_time = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_chatmessage")

    class Meta:
        verbose_name = "ChatMessage"
        verbose_name_plural = "ChatMessage"

    def __str__(self):
        return f"{self.text_message} - {self.sending_time} - {self.sender}"

