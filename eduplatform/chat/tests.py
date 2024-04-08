from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

from uuid import uuid4
from django.utils import timezone
from datetime import datetime
from mentorship.consts import (
    create_user, create_teacher, create_student,
    create_course, create_topic, create_article,
    create_test, create_question, create_answer,
    create_attempt, create_chatroom, create_message,
    create_sender, create_recipient)

from .serializers import ChatRoomSerializer, MessageSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class CreateChatRoomTest(APITestCase):
    def test_create_chatroom(self):
        url = reverse("chatroom-list")
        response = self.client.post(
            url,
            data={
                "name_chat": "Test-chat",
                "description_topics": "Test_description"},
            format="json")
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
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class DeleteChatRoomTest(APITestCase):
    def setUp(self):
        self.chatroom = create_chatroom()
    def test_delete_chatroom(self):
        url = reverse("chatroom-detail", args=[self.chatroom.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



class CreateMessageTest(APITestCase):
    def setUp(self):

        self.sender = create_sender()
        self.recipient = create_recipient()
        self.chatroom = create_chatroom()

    def test_create_message(self):
        url = reverse("message-list")
        response = self.client.post(
            url,
            data={
                "chatroom": self.chatroom.id,
                "text_message": "Text message",
                "sending_time": datetime.now().isoformat(),
                "sender": self.sender.id,
                "recipient": self.recipient.id},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadMessageTest(APITestCase):
    def setUp(self):
        self.sender = create_sender()
        self.recipient = create_recipient()
        self.chatroom = create_chatroom()
        self.message = create_message(chatroom_id=self.chatroom, sender_id=self.sender, recipient_id=self.recipient)

    def test_read_message_list(self):
        url = reverse("message-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_message_detail(self):
        url = reverse("message-detail", args=[self.message.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateMessageTest(APITestCase):
    def setUp(self):
        self.sender = create_sender()
        self.recipient = create_recipient()
        self.chatroom = create_chatroom()
        self.message = create_message(chatroom_id=self.chatroom, sender_id=self.sender, recipient_id=self.recipient)
        self.data = MessageSerializer(self.message).data
        self.data.update({"text_message": "course_name"})

    def test_update_message(self):
        url = reverse("message-detail", args=[self.message.id])
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class DeleteMessageTest(APITestCase):
    def setUp(self):
        self.sender = create_sender()
        self.recipient = create_recipient()
        self.chatroom = create_chatroom()
        self.message = create_message(chatroom_id=self.chatroom, sender_id=self.sender, recipient_id=self.recipient)
    def test_delete_message(self):
        url = reverse("message-detail", args=[self.message.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



