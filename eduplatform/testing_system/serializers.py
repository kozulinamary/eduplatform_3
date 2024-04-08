from rest_framework import serializers
from .models import Course, Topic, Test, Article, Question, Answer, Attempt
"""Нужно?   from django.contrib.auth.models import User"""


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class TopicSerializier(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"

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



class TopicArticleSerializer(serializers.ModelSerializer):
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
        return serializer.data


