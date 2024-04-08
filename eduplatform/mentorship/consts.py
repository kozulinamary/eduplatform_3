from .models import (User, Teacher, Student, Group)

from testing_system.models import (Course, Topic, Article, Test, Question, Answer, Attempt)
from chat.models import (ChatRoom, Message)
from .annotations import (
     UserAnnotation, TeacherAnnotation, StudentAnnotation,
     CourseAnnotation, TopicAnnotation, GroupAnnotation,
     ArticleAnnotation, TestAnnotation, QuestionAnnotation, AnswerAnnotation, AttemptAnnotation)
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

USER_DATA = {
    "password": "qwerty",
    "first_name": "Name_test",
    "last_name": "Surname_test",
    "email": "test@mail.ru",
}


def create_user() -> UserAnnotation:
    user = User.objects.create_user(
        password="qwerty",
        first_name="Name_test",
        last_name="Surname_test",
        email="test@mail.ru",)
    return user


def create_teacher(user_id) -> TeacherAnnotation:
    teacher = Teacher.objects.create(experience=10, user=user_id)
    return teacher

def create_student(user_id) -> StudentAnnotation:
    student = Student.objects.create(age=18, rating=55.55, user=user_id)
    return student

def create_course(teacher_id) -> CourseAnnotation:
    course = Course.objects.create(name="Test", teacher=teacher_id, price=1000)
    return course


def create_group(teacher_id, course_id) -> GroupAnnotation:
    group = Group.objects.create(group_name="Test", teacher=teacher_id, course=course_id)
    return group


def create_topic(course_id) -> TopicAnnotation:
    topic = Topic.objects.create(name="Topic", course=course_id, content="123456")
    return topic


def create_article(teacher_id, topic_id) -> ArticleAnnotation:
    article = Article.objects.create(
        title="Test",
        teacher=teacher_id,
        topic=topic_id,
        content="123456")
    return article

def create_test(teacher_id, topic_id) -> TestAnnotation:
    test = Test.objects.create(
        title="Test",
        topic=topic_id,
        teacher=teacher_id,
        description="12345",
        is_open=False)
    return test


def create_question(test_id) -> QuestionAnnotation:
    question = Question.objects.create(
        text="text_content",
        test=test_id,
        is_important=False)
    return question


def create_answer(question_id) -> AnswerAnnotation:
    answer = Answer.objects.create(
        text="answer_content",
        question=question_id,
        is_correct=False)
    return answer


def create_attempt(test_id, student_id) -> AttemptAnnotation:
    attempt = Attempt.objects.create(
        test=test_id,
        student=student_id,
        score=50)
    return attempt


def create_chatroom():
   chatroom = ChatRoom.objects.create(
        name_chat="Test_chat",
        description_topics="Description_Test_chat")
   return chatroom





def create_sender():
    sender = User.objects.create_user(
            email='test@mail.ru',
            password='qwerty',
            first_name='Name_test',
            last_name='Surname_test')
    return sender


def create_recipient():
    recipient = User.objects.create_user(
            email='recipient@example.com',
            password='password')
    return recipient




def create_message(chatroom_id, sender_id, recipient_id):
    message = Message.objects.create(
        chatroom=chatroom_id,
        text_message="Text message",
        sending_time=timezone.now(),
        sender=sender_id,
        recipient=recipient_id)
    return message



