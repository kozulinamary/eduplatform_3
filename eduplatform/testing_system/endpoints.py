from itertools import chain

from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import (
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
from .serializers import (
    AnswerSerializer,
    ArticleSerializer,
    AttemptSerializer,
    CourseSerializer,
    QuestionSerializer,
    RecommendationSerializer,
    TestAccessSerializer,
    TestSerializer,
    TopicArticleSerializer,
    TopicSerializier,
)

ALL_COURSES = Course.objects.all()
ALL_TOPICS = Topic.objects.all()
ALL_ARTICLES = Article.objects.all()
ALL_TESTS = Test.objects.all()
ALL_TESTS_ACCESS = TestAccess.objects.all()
ALL_QUESTIONS = Question.objects.all()
ALL_ANSWERS = Answer.objects.all()
ALL_ATTEMPTS = Attempt.objects.all()
ALL_RECOMMENDATION = Recommendation.objects.all()


class CourseViewSet(ModelViewSet):
    queryset = ALL_COURSES
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]


class TopicViewSet(ModelViewSet):
    queryset = ALL_TOPICS
    serializer_class = TopicSerializier
    permission_classes = [permissions.AllowAny]


class ArticleViewSet(ModelViewSet):
    queryset = ALL_ARTICLES
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]


class TestViewSet(ModelViewSet):
    queryset = ALL_TESTS
    serializer_class = TestSerializer
    permission_classes = [permissions.AllowAny]


class TestAccessViewSet(ModelViewSet):
    queryset = ALL_TESTS_ACCESS
    serializer_class = TestAccessSerializer
    permission_classes = [permissions.AllowAny]


class QuestionViewSet(ModelViewSet):
    queryset = ALL_QUESTIONS
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]


class AnswerViewSet(ModelViewSet):
    queryset = ALL_ANSWERS
    serializer_class = AnswerSerializer
    permission_classes = [permissions.AllowAny]


class AttemptViewSet(ModelViewSet):
    queryset = ALL_ATTEMPTS
    serializer_class = AttemptSerializer
    permission_classes = [permissions.AllowAny]


class CourseTopicAPIView(ListCreateAPIView):
    queryset = ALL_TOPICS
    serializer_class = TopicSerializier
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course = self.kwargs["id"]
        return Topic.objects.filter(course_id=course)


class TopicArticleAPIView(ListCreateAPIView):
    queryset = ALL_ARTICLES
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        topic = self.kwargs["id"]
        return Article.objects.filter(topic_id=topic)


class TestQuestionAPIView(ListCreateAPIView):
    queryset = ALL_QUESTIONS
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        test = self.kwargs["id"]
        return Question.objects.filter(test_id=test)


class QuestionAnswerAPIView(ListCreateAPIView):
    queryset = ALL_ANSWERS
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        question = self.kwargs["id"]
        return Answer.objects.filter(question_id=question)


class CourseContentAPIView(ListAPIView):
    serializer_class = TopicArticleSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        course_id = self.kwargs.get("id")
        topics = Topic.objects.filter(course_id=course_id)
        articles = Article.objects.filter(topic__in=topics)
        content = list(chain(topics, articles))
        return content


class RecommendationViewSet(ModelViewSet):
    queryset = ALL_RECOMMENDATION
    serializer_class = RecommendationSerializer
    permission_classes = [permissions.AllowAny]
