from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .endpoints import ChatRoomViewSet, MessageViewSet, ChatRoomMessageAPIView




router = DefaultRouter()
router.register("chatroom", ChatRoomViewSet)
router.register("message", MessageViewSet)




urlpatterns = [
    path("", include(router.urls)),
    path("chatroom/<id>/message", ChatRoomMessageAPIView.as_view(), name="chatroom_message"),
]

