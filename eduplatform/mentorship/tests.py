<<<<<<< HEAD
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .consts import (
    USER_DATA,
    create_course,
    create_group,
    create_message,
    create_recipient_2,
    create_sender_2,
    create_student,
    create_teacher,
    create_user,
)
from .serializers import (
    GroupSerializer,
    MessageSerializer,
    StudentSerializer,
    TeacherSerializer,
    UserSerializer,
)

__all__ = {
    "CreateUserTest",
    "ReadUserTest",
    "UpdateUserTest",
    "DeleteUserTest",
    "CreateTeacherTest",
    "ReadTeacherTest",
    "UpdateTeacherTest",
    "DeleteTeacherTest",
    "CreateStudentTest",
    "ReadStudentTest",
    "UpdateStudentTest",
    "DeleteStudentTest",
    "CreateGroupTest",
    "ReadGroupTest",
    "UpdateGroupTest",
    "DeleteGroupTest",
    "CreateMessageTest",
    "ReadMessageTest",
    "UpdateMessageTest",
    "DeleteMessageTest",
}


class CreateUserTest(APITestCase):
=======
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from .consts import (
    USER_DATA, create_user, create_teacher,
    create_student, create_course, create_group)
from .serializers import (
    UserSerializer, TeacherSerializer,
    StudentSerializer, GroupSerializer)

__all__ = {"CreateUserTest", "ReadUserTest", "UpdateUserTest", "DeleteUserTest",
           "CreateTeacherTest", "ReadTeacherTest", "UpdateTeacherTest", "DeleteTeacherTest",
           "CreateStudentTest", "ReadStudentTest", "UpdateStudentTest", "DeleteStudentTest",
           "CreateGroupTest", "ReadGroupTest", "UpdateGroupTest", "DeleteGroupTest"
           }
class CreateUserTest(APITestCase):

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    def test_create_user(self):
        url = reverse("user-list")
        response = self.client.post(url, data=USER_DATA, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_read_user_list(self):
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_user_detail(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class UpdateUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.data = UserSerializer(self.user).data
        self.data.update({"first_name": "newName_test"})

<<<<<<< HEAD
=======

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    def test_update_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class DeleteUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_delete_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


<<<<<<< HEAD
=======

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class CreateTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_create_teacher(self):
        url = reverse("teacher-list")
<<<<<<< HEAD
        response = self.client.post(url, data={"experience": 12, "user": self.user.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


=======
        response = self.client.post(
            url,
            data={"experience": 12, "user": self.user.id},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class ReadTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()

        self.teacher = create_teacher(self.user)

<<<<<<< HEAD
=======


>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    def test_read_teacher_list(self):
        url = reverse("teacher-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_teacher_detail(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()

        self.teacher = create_teacher(self.user)
        self.data = TeacherSerializer(self.teacher).data
        self.data.update({"experience": "20"})

    def test_update_teacher(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class DeleteTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()

        self.teacher = create_teacher(self.user)
<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    def test_delete_teacher(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# Create your tests here.
class CreateStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_create_student(self):
        url = reverse("student-list")
<<<<<<< HEAD
        response = self.client.post(url, data={"age": 22, "user": self.user.id, "rating": 85.30}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


=======
        response = self.client.post(
            url,
            data={"age": 22, "user": self.user.id, "rating": 85.30},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class ReadStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()

        self.student = create_student(self.user)

<<<<<<< HEAD
=======


>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    def test_read_student_list(self):
        url = reverse("student-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_student_detail(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class UpdateStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)
        self.data = StudentSerializer(self.student).data
        self.data.update({"age": 32})

    def test_update_student(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class DeleteStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()

        self.student = create_student(self.user)
<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    def test_delete_student(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()

        self.student = create_student(self.user)
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)

    def test_create_group(self):
        url = reverse("group-list")
<<<<<<< HEAD
        response = self.client.post(url, data={"group_name": "Test", "teacher": self.teacher.id, "student": [self.student.id], "course": self.course.id}, format="json")
=======
        response = self.client.post(
            url,
            data={
                "group_name": "Test",
                "teacher": self.teacher.id,
                "student": [self.student.id],
                "course": self.course.id},
            format="json")
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()

        self.student = create_student(self.user)
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.group = create_group(teacher_id=self.teacher, course_id=self.course)

    def test_read_group_list(self):
        url = reverse("group-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

<<<<<<< HEAD
=======

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    def test_read_group_detail(self):
        url = reverse("group-detail", args=[self.group.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


<<<<<<< HEAD
=======



>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class UpdateGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()

        self.student = create_student(self.user)
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.group = create_group(teacher_id=self.teacher, course_id=self.course)
        self.data = GroupSerializer(self.group).data
        self.data.update({"group_name": "newName"})

    def test_update_group(self):
        url = reverse("group-detail", args=[self.group.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()

        self.student = create_student(self.user)
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.group = create_group(teacher_id=self.teacher, course_id=self.course)
<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    def test_delete_group(self):
        url = reverse("group-detail", args=[self.group.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
<<<<<<< HEAD


def generate_random_email():
    random_string = "".join(random.choices(string.ascii_lowercase, k=5))
    return f"{random_string}@example.com"


class CreateMessageTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.sender = create_sender_2()
        self.recipient = create_recipient_2()

    def test_create_message(self):
        url = reverse("message-list")
        response = self.client.post(url, data={"sender": self.sender.id, "recipients": [self.recipient.id], "topic": "Topic", "text": "Text"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadMessageTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.sender = create_sender_2()
        self.recipient = create_recipient_2()
        self.message = create_message(sender=self.sender, recipient=self.recipient)

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
        self.user = create_user()
        self.sender = create_sender_2()
        self.recipient = create_recipient_2()
        self.message = create_message(sender=self.sender, recipient=self.recipient)
        self.data = MessageSerializer(self.message).data
        self.data.update({"text": "newText"})

    def test_update_message(self):
        url = reverse("message-detail", args=[self.message.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteMessageTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.sender = create_sender_2()
        self.recipient = create_recipient_2()
        self.message = create_message(sender=self.sender, recipient=self.recipient)

    def test_delete_message(self):
        url = reverse("message-detail", args=[self.message.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
