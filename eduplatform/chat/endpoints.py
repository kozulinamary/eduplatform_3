from rest_framework import permissions
from itertools import chain
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from django.db.models import Subquery, OuterRef

from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer


class ChatRoomViewSet(ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.AllowAny]


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]




class ChatRoomMessageAPIView(ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        chatroom_id = self.kwargs["id"]
        return Message.objects.filter(chatroom_id=chatroom_id)




