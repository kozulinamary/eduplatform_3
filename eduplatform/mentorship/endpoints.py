from itertools import chain

from django.http import HttpResponse
from rest_framework import mixins, permissions
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Group, Message, Student, Teacher, User
from .serializers import (
    GroupSerializer,
    MessageSerializer,
    RegisterSerializer,
    StudentSerializer,
    TeacherSerializer,
    TeacherStudentSerializer,
    UserSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


class GroupStudentAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        group = self.kwargs["id"]
        return Student.objects.filter(group__in=group)


class GroupMembersAPIView(ListAPIView):
    serializer_class = TeacherStudentSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        group = self.kwargs["id"]
        students = Student.objects.filter(group__in=group)
        teacher = Teacher.objects.filter(group=group)
        members = list(chain(set(students), set(teacher)))
        return members


class RegisterUserViewSet(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(f"User{serializer.data['email']} created!", status=201)


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]
