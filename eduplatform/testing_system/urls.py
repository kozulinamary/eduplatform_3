<<<<<<< HEAD
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .endpoints import (
    AnswerViewSet,
    ArticleViewSet,
    AttemptViewSet,
    CourseContentAPIView,
    CourseTopicAPIView,
    CourseViewSet,
    QuestionAnswerAPIView,
    QuestionViewSet,
    RecommendationViewSet,
    TestAccessViewSet,
    TestQuestionAPIView,
    TestViewSet,
    TopicArticleAPIView,
    TopicViewSet,
)
=======
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .endpoints import (CourseViewSet, TopicViewSet,
                        ArticleViewSet, TestViewSet,
                        QuestionViewSet, AnswerViewSet,
                        AttemptViewSet, CourseTopicAPIView,
                        TopicArticleAPIView, TestQuestionAPIView,
                        QuestionAnswerAPIView, CourseContentAPIView)
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a

router = DefaultRouter()
router.register("course", CourseViewSet)
router.register("topic", TopicViewSet)
router.register("article", ArticleViewSet)
router.register("test", TestViewSet)
<<<<<<< HEAD
router.register("test_access", TestAccessViewSet, basename="test_access")
router.register("question", QuestionViewSet)
router.register("answer", AnswerViewSet)
router.register("attempt", AttemptViewSet)
router.register("recommendation", RecommendationViewSet)
=======
router.register("question", QuestionViewSet)
router.register("answer", AnswerViewSet)
router.register("attempt", AttemptViewSet)


>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a


urlpatterns = [
    path("", include(router.urls)),
    path("course/<id>/topics/", CourseTopicAPIView.as_view(), name="course_topics"),
    path("topic/<id>/articles/", TopicArticleAPIView.as_view(), name="topic_articles"),
    path("test/<id>/questions/", TestQuestionAPIView.as_view(), name="test_questions"),
    path("question/<id>/answers/", QuestionAnswerAPIView.as_view(), name="question_answers"),
    path("course/<id>/content/", CourseContentAPIView.as_view(), name="course_content"),
<<<<<<< HEAD
]
=======

]
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
