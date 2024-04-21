"""
URL configuration for eduplatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

<<<<<<< HEAD
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
=======
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .endpoints import UserViewSet, TeacherViewSet, StudentViewSet, GroupViewSet, GroupStudentAPIView,\
    GroupMembersAPIView, RegisterUserViewSet, MessageViewSet

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a

router = DefaultRouter()
router.register("user", UserViewSet)
router.register("teacher", TeacherViewSet)
router.register("student", StudentViewSet)
router.register("group", GroupViewSet)
<<<<<<< HEAD
router.register("register", RegisterUserViewSet, basename="user_register")
router.register("message", MessageViewSet, basename="message")
router.register("register_user", RegisterUserViewSet, basename="register_user")


=======
router.register('register', RegisterUserViewSet, basename="user_register")
router.register("site_user", MessageViewSet, basename="message")
router.register("register_user", RegisterUserViewSet, basename="register_user")



>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
urlpatterns = [
    path("", include(router.urls)),
    path("group/<id>/students/", GroupStudentAPIView.as_view(), name="group_students"),
    path("group/<id>/members/", GroupMembersAPIView.as_view(), name="group_members"),
<<<<<<< HEAD
=======

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
]
