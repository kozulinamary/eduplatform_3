
from datetime import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse
from mentorship.consts import (
    create_answer,
    create_article,
    create_attempt,
    create_chat_message,
    create_chatroom,
    create_course,
    create_question,
    create_recipient,
    create_sender,
    create_student,
    create_teacher,
    create_test,
    create_topic,
    create_user,
)
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import ChatMessageSerializer, ChatRoomSerializer

User = get_user_model()


__all__ = {
    "CreateChatRoomTest",
    "ReadChatRoomTest",
    "UpdateChatRoomTest",
    "DeleteChatRoomTest",
    "CreateChatMessageTest",
    "ReadChatMessageTest",
    "UpdateChatMessageTest",
    "DeleteChatMessageTest",
}


class CreateChatRoomTest(APITestCase):
    def test_create_chatroom(self):
        url = reverse("chatroom-list")
        response = self.client.post(url, data={"name_chat": "Test-chat", "description_topics": "Test_description"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class ReadChatRoomTest(APITestCase):
    def setUp(self):
        self.chatroom = create_chatroom()

    def test_read_chatroom_list(self):
        url = reverse("chatroom-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_chatroom_detail(self):
        url = reverse("chatroom-detail", args=[self.chatroom.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class UpdateChatRoomTest(APITestCase):
    def setUp(self):
        self.chatroom = create_chatroom()
        self.data = ChatRoomSerializer(self.chatroom).data
        self.data.update({"description_topics": "New_description_chat"})

    def test_update_chatroom(self):
        url = reverse("chatroom-detail", args=[self.chatroom.id])

        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteChatRoomTest(APITestCase):
    def setUp(self):
        self.chatroom = create_chatroom()
    def test_delete_chatroom(self):
        url = reverse("chatroom-detail", args=[self.chatroom.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateChatMessageTest(APITestCase):
    def setUp(self):

        self.sender = create_sender()
        self.recipient = create_recipient()
        self.chatroom = create_chatroom()

    def test_create_chat_message(self):
        url = reverse("chatmessage-list")
        response = self.client.post(
            url,
            data={"chatroom": self.chatroom.id, "text_message": "Text message", "sending_time": datetime.now().isoformat(), "sender": self.sender.id, "recipient": self.recipient.id},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadChatMessageTest(APITestCase):
    def setUp(self):
        self.sender = create_sender()
        self.recipient = create_recipient()
        self.chatroom = create_chatroom()
        self.chat_message = create_chat_message(chatroom_id=self.chatroom, sender_id=self.sender, recipient_id=self.recipient)

    def test_read_chat_message_list(self):
        url = reverse("chatmessage-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_chat_message_detail(self):
        url = reverse("chatmessage-detail", args=[self.chat_message.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class UpdateChatMessageTest(APITestCase):
    def setUp(self):
        self.sender = create_sender()
        self.recipient = create_recipient()
        self.chatroom = create_chatroom()
        self.chat_message = create_chat_message(chatroom_id=self.chatroom, sender_id=self.sender, recipient_id=self.recipient)
        self.data = ChatMessageSerializer(self.chat_message).data
        self.data.update({"text_message": "course_name"})

    def test_update_chat_message(self):
        url = reverse("chatmessage-detail", args=[self.chat_message.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteChatMessageTest(APITestCase):
    def setUp(self):
        self.sender = create_sender()
        self.recipient = create_recipient()
        self.chatroom = create_chatroom()
        self.chat_message = create_chat_message(chatroom_id=self.chatroom, sender_id=self.sender, recipient_id=self.recipient)

    def test_delete_chat_message(self):
        url = reverse("chatmessage-detail", args=[self.chat_message.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

