from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .endpoints import ChatMessageViewSet, ChatRoomChatMessageAPIView, ChatRoomViewSet

router = DefaultRouter()
router.register("chatroom", ChatRoomViewSet)
router.register("chat_message", ChatMessageViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("chatroom/<id>/chat_message", ChatRoomChatMessageAPIView.as_view(), name="chatroom_chat_message"),
]

