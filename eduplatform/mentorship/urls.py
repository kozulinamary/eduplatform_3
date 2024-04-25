from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .endpoints import (
    GroupMembersAPIView,
    GroupStudentAPIView,
    GroupViewSet,
    MessageViewSet,
    RegisterUserViewSet,
    StudentViewSet,
    TeacherViewSet,
    UserViewSet,
)


router = DefaultRouter()
router.register("user", UserViewSet)
router.register("teacher", TeacherViewSet)
router.register("student", StudentViewSet)
router.register("group", GroupViewSet)

router.register("register", RegisterUserViewSet, basename="user_register")
router.register("message", MessageViewSet, basename="message")
router.register("register_user", RegisterUserViewSet, basename="register_user")



urlpatterns = [
    path("", include(router.urls)),
    path("group/<id>/students/", GroupStudentAPIView.as_view(), name="group_students"),
    path("group/<id>/members/", GroupMembersAPIView.as_view(), name="group_members"),

]
