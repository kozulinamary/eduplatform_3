
from chat.models import ChatMessage, ChatRoom
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from testing_system.models import (
    Answer,
    Article,
    Attempt,
    Course,
    Question,
    Recommendation,
    Test,
    TestAccess,
    Topic,
)

from .annotations import (
    AnswerAnnotation,
    ArticleAnnotation,
    AttemptAnnotation,
    ChatMessageAnnotation,
    ChatRoomAnnotation,
    CourseAnnotation,
    GroupAnnotation,
    MessageAnnotation,
    QuestionAnnotation,
    RecommendationAnnotation,
    StudentAnnotation,
    TeacherAnnotation,
    TestAccessAnnotation,
    TestAnnotation,
    TopicAnnotation,
    UserAnnotation,
)
from .models import Group, Message, Student, Teacher, User


USER_DATA = {
    "password": "qwerty",
    "first_name": "Name_test",
    "last_name": "Surname_test",
    "email": "test@mail.ru",
}


def create_user() -> UserAnnotation:
    email = "test@mail.ru"
    try:
        user = User.objects.get(email=email)
    except ObjectDoesNotExist:
        user = User.objects.create_user(email=email, password="qwerty", first_name="Name_test", last_name="Surname_test")

    return user


def create_teacher(user_id) -> TeacherAnnotation:
    teacher = Teacher.objects.create(experience=10, user=user_id)
    return teacher



def create_teacher_2(user_id) -> TeacherAnnotation:
    teacher_2 = Teacher.objects.create(experience=20, user=user_id)
    return teacher_2



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



def create_test(teacher_id, topic_id) -> TestAnnotation:
    test = Test.objects.create(title="Test", topic=topic_id, teacher=teacher_id, description="12345", is_open=False)
    return test


def create_test_access(test_id, shared_with_teacher_id) -> TestAccessAnnotation:
    test_access = TestAccess.objects.create(
        test=test_id,
        shared_with_teacher=shared_with_teacher_id,
    )
    return test_access



def create_article(teacher_id, topic_id) -> ArticleAnnotation:
    article = Article.objects.create(
        title="Test",
        teacher=teacher_id,
        topic=topic_id,
        content="123456",
    )
    return article


def create_question(test_id) -> QuestionAnnotation:
    question = Question.objects.create(text="text_content", test=test_id, is_important=False)

    return question


def create_answer(question_id) -> AnswerAnnotation:

    answer = Answer.objects.create(text="answer_content", question=question_id, is_correct=False)
    return answer


def create_attempt(test_id, student_id) -> AttemptAnnotation:
    attempt = Attempt.objects.create(test=test_id, student=student_id, score=50)
    return attempt


def create_chatroom() -> ChatRoomAnnotation:
    chatroom = ChatRoom.objects.create(name_chat="Test_chat", description_topics="Description_Test_chat")
    return chatroom


def create_sender():
    sender = User.objects.create_user(email="test@mail.ru", password="qwerty", first_name="Name_test", last_name="Surname_test")

    return sender


def create_recipient():
    recipient = User.objects.create_user(email="recipient@example.com", password="password")
    return recipient


def create_sender_2():
    sender_2 = User.objects.create_user(email="teeest@mail.ru", password="qwerty", first_name="Name_test", last_name="Surname_test")
    return sender_2


def create_recipient_2():
    recipient_2 = User.objects.create_user(email="recipient111@example.com", password="password")
    return recipient_2


def create_chat_message(chatroom_id, sender_id, recipient_id) -> ChatMessageAnnotation:
    chat_message = ChatMessage.objects.create(chatroom=chatroom_id, text_message="Text message", sending_time=timezone.now(), sender=sender_id, recipient=recipient_id)
    return chat_message


def create_recommendation(student_id, test_id, course_id, article_id) -> RecommendationAnnotation:
    recommendation = Recommendation.objects.create(
        text="recommendation to",
        student=Student.objects.get(pk=student_id),
        test=Test.objects.get(pk=test_id),
    )
    recommendation.recommended_courses.add(Course.objects.get(pk=course_id))
    recommendation.recommended_articles.add(Article.objects.get(pk=article_id))

    return recommendation


def create_message(sender, recipient) -> MessageAnnotation:
    message_2 = Message.objects.create(sender_id=sender.id, topic="New_topic", text="New_text")
    message_2.recipients.add(recipient.id)
    return message_2

