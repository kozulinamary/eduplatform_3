<<<<<<< HEAD
from django.urls import reverse
from mentorship.consts import (
    create_answer,
    create_article,
    create_attempt,
    create_course,
    create_question,
    create_recommendation,
    create_student,
    create_teacher,
    create_teacher_2,
    create_test,
    create_test_access,
    create_topic,
    create_user,
)
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import (
    AnswerSerializer,
    ArticleSerializer,
    AttemptSerializer,
    CourseSerializer,
    QuestionSerializer,
    RecommendationSerializer,
    TestAccessSerializer,
    TestSerializer,
    TopicSerializier,
)

__all__ = {
    "CreateCourseTest",
    "ReadCourseTest",
    "UpdateCourseTest",
    "DeleteCourseTest",
    "CreateTopicTest",
    "ReadTopicTest",
    "UpdateTopicTest",
    "DeleteTopicTest",
    "CreateArticleTest",
    "ReadArticleTest",
    "UpdateArticleTest",
    "DeleteArticleTest",
    "CreateTestTest",
    "ReadTestTest",
    "UpdateTestTest",
    "DeleteTestTest",
    "CreateQuestionTest",
    "ReadQuestionTest",
    "UpdateQuestionTest",
    "DeleteQuestionTest",
    "CreateAnswerTest",
    "ReadAnswerTest",
    "UpdateAnswerTest",
    "DeleteAnswerTest",
    "CreateAttemptTest",
    "ReadAttemptTest",
    "UpdateAttemptTest",
    "DeleteAttemptTest",
    "CreateTestAccessTest",
    "ReadTestAccessTest",
    "UpdateTestAccessTest",
    "DeleteTestAccessTest",
}


=======
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from mentorship.consts import (
    create_user, create_teacher, create_student,
    create_course, create_topic, create_article,
    create_test, create_question, create_answer,
    create_attempt)
from .serializers import CourseSerializer, TopicSerializier, TestSerializer, QuestionSerializer, AnswerSerializer, AttemptSerializer, ArticleSerializer



__all__={"CreateCourseTest", "ReadCourseTest", "UpdateCourseTest", "DeleteCourseTest",
         "CreateTopicTest", "ReadTopicTest", "UpdateTopicTest", "DeleteTopicTest",
         "CreateArticleTest", "ReadArticleTest", "UpdateArticleTest", "DeleteArticleTest",
         "CreateTestTest", "ReadTestTest", "UpdateTestTest", "DeleteTestTest",
         "CreateQuestionTest", "ReadQuestionTest", "UpdateQuestionTest", "DeleteQuestionTest",
         "CreateAnswerTest", "ReadAnswerTest", "UpdateAnswerTest", "DeleteAnswerTest",
         "CreateAttemptTest", "ReadAttemptTest", "UpdateAttemptTest", "DeleteAttemptTest"}
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class CreateCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)

<<<<<<< HEAD
    def test_create_course(self):
        url = reverse("course-list")
        response = self.client.post(url, data={"course_name": "Test", "teacher": self.teacher.id, "price": 1000}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


=======

    def test_create_course(self):
        url = reverse("course-list")
        response = self.client.post(
            url,
            data={
                "course_name": "Test",
                "teacher": self.teacher.id,
                "price": 1000},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class ReadCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)

    def test_read_course_list(self):
        url = reverse("course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_course_detail(self):
        url = reverse("course-detail", args=[self.course.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class UpdateCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.data = CourseSerializer(self.course).data
        self.data.update({"course_name": "NewTestName"})

    def test_update_course(self):
        url = reverse("course-detail", args=[self.course.id])
<<<<<<< HEAD
        response = self.client.put(url, self.data, format="json")
=======
        response = self.client.put(url, self.data, format='json')
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    def test_delete_course(self):
        url = reverse("course-detail", args=[self.course.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)

    def test_create_topic(self):
        url = reverse("topic-list")
<<<<<<< HEAD
        response = self.client.post(url, data={"name": "Test", "course": self.course.id, "content": 123456}, format="json")
=======
        response = self.client.post(
            url,
            data={
                "name": "Test",
                "course": self.course.id,
                "content": 123456},
            format="json")
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_read_topic_list(self):
        url = reverse("topic-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_topic_detail(self):
        url = reverse("topic-detail", args=[self.topic.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.data = TopicSerializier(self.topic).data
        self.data.update({"name": "NewTestName"})

    def test_update_topic(self):
        url = reverse("topic-detail", args=[self.topic.id])
<<<<<<< HEAD
        response = self.client.put(url, self.data, format="json")
=======
        response = self.client.put(url, self.data, format='json')
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_delete_topic(self):
        url = reverse("topic-detail", args=[self.topic.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateArticleTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
<<<<<<< HEAD
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a

    def test_create_article(self):
        url = reverse("article-list")
        response = self.client.post(
            url,
            data={
                "title": "Test",
                "topic": self.topic.id,
                "teacher": self.teacher.id,
<<<<<<< HEAD
                "content": "123456",
                "test": self.test.id,
                "course": self.course.id,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


=======
                "content": "123456"},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class ReadArticleTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.article = create_article(teacher_id=self.teacher, topic_id=self.topic)
<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    def test_read_article_list(self):
        url = reverse("article-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_article_detail(self):
        url = reverse("article-detail", args=[self.article.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class UpdateArticleTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.article = create_article(teacher_id=self.teacher, topic_id=self.topic)
<<<<<<< HEAD
        self.data = ArticleSerializer(self.article).data
=======
        self.data = TopicSerializier(self.topic).data
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
        self.data.update({"title": "NewArticleTitle"})

    def test_update_article(self):
        url = reverse("article-detail", args=[self.article.id])
<<<<<<< HEAD
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


=======
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class DeleteArticleTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.article = create_article(teacher_id=self.teacher, topic_id=self.topic)

    def test_delete_article(self):
        url = reverse("article-detail", args=[self.article.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


<<<<<<< HEAD
=======


>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class CreateTestTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_create_test(self):
        url = reverse("test-list")
<<<<<<< HEAD
        response = self.client.post(url, data={"title": "Test", "topic": self.topic.id, "teacher": self.teacher.id, "description": "12345", "is_open": False}, format="json")
=======
        response = self.client.post(
            url,
            data={
                "title": "Test",
                "topic": self.topic.id,
                "teacher": self.teacher.id,
                "description": "12345",
                "is_open": False},
            format="json")
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTestTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)

    def test_read_test_list(self):
        url = reverse("test-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_test_detail(self):
        url = reverse("test-detail", args=[self.test.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


<<<<<<< HEAD
=======

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class UpdateTestTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
<<<<<<< HEAD
        self.data = TestSerializer(self.test).data
=======
        self.data =TestSerializer(self.test).data
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
        self.data.update({"title": "NewTestTitle"})

    def test_update_test(self):
        url = reverse("test-detail", args=[self.test.id])
<<<<<<< HEAD
        response = self.client.put(url, self.data, format="json")
=======
        response = self.client.put(url, self.data, format='json')
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTestTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)

    def test_delete_test(self):
        url = reverse("test-detail", args=[self.test.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


<<<<<<< HEAD
class CreateTestAccessTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.shared_with_teacher = create_teacher(self.user)

    def test_create_test_access(self):
        url = reverse("test_access-list")
        response = self.client.post(url, data={"test": self.test.id, "shared_with_teacher": self.shared_with_teacher.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTestAccessTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.shared_with_teacher = create_teacher(self.user)
        self.test_access = create_test_access(test_id=self.test, shared_with_teacher_id=self.shared_with_teacher)

    def test_read_test_access_list(self):
        url = reverse("test_access-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_test_access_detail(self):
        url = reverse("test_access-detail", args=[self.test_access.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTestAccessTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.shared_with_teacher = create_teacher(self.user)
        self.test_access = create_test_access(test_id=self.test, shared_with_teacher_id=self.shared_with_teacher)
        self.data = TestAccessSerializer(self.test_access).data
        new_teacher = create_teacher_2(create_user())
        self.data.update({"shared_with_teacher": new_teacher.id})

    def test_update_test_access(self):
        url = reverse("test_access-detail", args=[self.test_access.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTestAccessTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.shared_with_teacher = create_teacher(self.user)
        self.test_access = create_test_access(test_id=self.test, shared_with_teacher_id=self.shared_with_teacher)

    def test_delete_test_access(self):
        url = reverse("test_access-detail", args=[self.test_access.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class CreateQuestionTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)

    def test_create_question(self):
        url = reverse("question-list")
<<<<<<< HEAD
        response = self.client.post(url, data={"text": "question_text", "test": self.test.id, "is_important": False}, format="json")
=======
        response = self.client.post(
            url,
            data={
                "text": "question_text",
                "test": self.test.id,
                "is_important": False},
            format="json")
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadQuestionTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.question = create_question(self.test)

    def test_read_question_list(self):
        url = reverse("question-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_question_detail(self):
        url = reverse("question-detail", args=[self.question.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


<<<<<<< HEAD
=======

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class UpdateQuestionTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.question = create_question(test_id=self.test)
        self.data = QuestionSerializer(self.question).data
        self.data.update({"text": "NewText"})

    def test_update_question(self):
        url = reverse("question-detail", args=[self.question.id])
<<<<<<< HEAD
        response = self.client.put(url, self.data, format="json")
=======
        response = self.client.put(url, self.data, format='json')
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteQuestionTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.question = create_question(test_id=self.test)

    def test_delete_question(self):
        url = reverse("question-detail", args=[self.question.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


<<<<<<< HEAD
=======

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class CreateAnswerTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.question = create_question(test_id=self.test)

<<<<<<< HEAD
    def test_create_answer(self):
        url = reverse("answer-list")
        response = self.client.post(url, data={"text": "answer_text", "question": self.question.id, "is_correct": False}, format="json")
=======

    def test_create_answer(self):
        url = reverse("answer-list")
        response = self.client.post(
            url,
            data={
                "text": "answer_text",
                "question": self.question.id,
                "is_correct": False},
            format="json")
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadAnswerTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.question = create_question(test_id=self.test)
        self.answer = create_answer(self.question)

    def test_read_answer_list(self):
        url = reverse("answer-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_answer_detail(self):
        url = reverse("answer-detail", args=[self.answer.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateAnswerTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.question = create_question(test_id=self.test)
        self.answer = create_answer(self.question)
        self.data = AnswerSerializer(self.answer).data
        self.data.update({"text": "New_answer_Text"})

    def test_update_answer(self):
        url = reverse("answer-detail", args=[self.answer.id])
<<<<<<< HEAD
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


=======
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class DeleteAnswerTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.question = create_question(test_id=self.test)
        self.answer = create_answer(self.question)

    def test_delete_answer(self):
        url = reverse("answer-detail", args=[self.answer.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class CreateAttemptTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.student = create_student(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)

<<<<<<< HEAD
    def test_create_attempt(self):
        url = reverse("attempt-list")
        response = self.client.post(url, data={"test": self.test.id, "student": self.student.id, "score": 50}, format="json")
=======


    def test_create_attempt(self):
        url = reverse("attempt-list")
        response = self.client.post(
            url,
            data={
                "test": self.test.id,
                "student": self.student.id,
                "score": 50},
            format="json")
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadAttemptTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.student = create_student(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.attempt = create_attempt(test_id=self.test, student_id=self.student)

<<<<<<< HEAD
=======

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    def test_read_attempt_list(self):
        url = reverse("attempt-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_attempt_detail(self):
        url = reverse("attempt-detail", args=[self.attempt.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateAttemptTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.student = create_student(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.attempt = create_attempt(test_id=self.test, student_id=self.student)
        self.data = AttemptSerializer(self.attempt).data
        self.data.update({"score": 60})

    def test_update_attempt(self):
        url = reverse("attempt-detail", args=[self.attempt.id])
<<<<<<< HEAD
        response = self.client.put(url, self.data, format="json")
=======
        response = self.client.put(url, self.data, format='json')
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteAttemptTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.student = create_student(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.attempt = create_attempt(test_id=self.test, student_id=self.student)

    def test_delete_attempt(self):
        url = reverse("attempt-detail", args=[self.attempt.id])
        response = self.client.delete(url)
<<<<<<< HEAD
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateRecommendationTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.article = create_article(teacher_id=self.teacher, topic_id=self.topic)

    def test_create_recommendation(self):
        url = reverse("recommendation-list")
        response = self.client.post(
            url, data={"text": "recommendation to", "student": self.student.id, "test": self.test.id, "recommended_courses": [self.course.id], "recommended_articles": [self.article.id]}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadRecommendationTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.article = create_article(teacher_id=self.teacher, topic_id=self.topic)

        self.recommendation = create_recommendation(student_id=self.student.id, test_id=self.test.id, course_id=self.course.id, article_id=self.article.id)

    def test_read_recommendation_list(self):
        url = reverse("recommendation-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_recommendation_detail(self):
        url = reverse("recommendation-detail", args=[self.recommendation.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateRecommendationTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.article = create_article(teacher_id=self.teacher, topic_id=self.topic)

        self.recommendation = create_recommendation(student_id=self.student.id, test_id=self.test.id, course_id=self.course.id, article_id=self.article.id)
        self.data = RecommendationSerializer(self.recommendation).data
        self.data.update({"text": "New_text"})

    def test_update_recommendation(self):
        url = reverse("recommendation-detail", args=[self.recommendation.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteRecommendationTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_test(teacher_id=self.teacher, topic_id=self.topic)
        self.article = create_article(teacher_id=self.teacher, topic_id=self.topic)

        self.recommendation = create_recommendation(student_id=self.student.id, test_id=self.test.id, course_id=self.course.id, article_id=self.article.id)

    def test_delete_recommendation(self):
        url = reverse("recommendation-detail", args=[self.recommendation.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
=======
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
