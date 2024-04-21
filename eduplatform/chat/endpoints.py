from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import ChatMessage, ChatRoom
from .serializers import ChatMessageSerializer, ChatRoomSerializer


class ChatRoomViewSet(ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.AllowAny]


class ChatMessageViewSet(ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.AllowAny]


class ChatRoomChatMessageAPIView(ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        chatroom_id = self.kwargs["id"]
        return ChatMessage.objects.filter(chatroom_id=chatroom_id)
