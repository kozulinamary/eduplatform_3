from rest_framework import serializers

from .models import Group, Message, Student, Teacher, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


"""Было  class TeacherStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
    def to_representation(self, object):

        match isinstance(object, Student):
            case True:
                serializer = StudentSerializer(object)
            case False:
                serializer = TeacherSerializer(object)
            case _:
                raise Exception("Nothing to serialize")
        return serializer.data"""


class TeacherStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

    def to_representation(self, obj):
        if isinstance(obj, Student):
            serializer = StudentSerializer(obj)
        elif isinstance(obj, Teacher):
            serializer = TeacherSerializer(obj)
        else:
            raise Exception("Nothing to serialize")

        return serializer.data


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        ModelClass = User

        try:
            user = ModelClass.objects.create_user(**validated_data)
        except TypeError:
            msg = (
                "Got a `TypeError` when calling `%s.%s.create()`. "
                "This may be because you have a writable field on the "
                "serializer class that is not a valid argument to "
                "`%s.%s.create()`. You may need to make the field "
                "read-only, or override the %s.create() method to handle "
                "this correctly."
                % (
                    ModelClass.__name__,
                    ModelClass._default_manager.name,
                    ModelClass.__name__,
                    ModelClass._default_manager.name,
                    self.__class__.__name__,
                )
            )
            raise TypeError(msg)

        return user


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
