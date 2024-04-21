from rest_framework import serializers
<<<<<<< HEAD

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
=======
from .models import Course, Topic, Test, Article, Question, Answer, Attempt
"""Нужно?   from django.contrib.auth.models import User"""
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class TopicSerializier(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"

<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"

<<<<<<< HEAD

class TestAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAccess
        fields = "__all__"


=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = "__all__"


<<<<<<< HEAD
""" Было    class TopicArticleSerializer(serializers.ModelSerializer):
=======

class TopicArticleSerializer(serializers.ModelSerializer):
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    class Meta:
        model = Topic

    def to_representation(self, object):
        match isinstance(object, Topic):
            case True:
                serializer = TopicSerializier(object)
            case False:
                serializer = ArticleSerializer(object)
            case _:
                raise Exception("Nothing to serialize. Chooses are: Topic or Article instances.")
<<<<<<< HEAD
        return serializer.data"""


class TopicArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic

    def to_representation(self, object):
        if isinstance(object, Topic):
            serializer = TopicSerializier(object)
        elif isinstance(object, Article):
            serializer = ArticleSerializer(object)
        else:
            raise Exception("Nothing to serialize. Chooses are: Topic or Article instances.")
        return serializer.data


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = "__all__"
=======
        return serializer.data


>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
