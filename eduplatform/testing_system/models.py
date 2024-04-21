from django.db import models
<<<<<<< HEAD
from mentorship.mixins import DateTimeMixin
from mentorship.models import Student, Teacher
=======
from mentorship.models import Teacher, Student
from mentorship.mixins import DateTimeMixin
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a


class Course(models.Model, DateTimeMixin):
    name = models.CharField(max_length=100, default="course_name")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.pk} - {self.name} - {self.price}$"
<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"

<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class Topic(models.Model, DateTimeMixin):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"


<<<<<<< HEAD
=======

class Article(models.Model, DateTimeMixin):
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"


>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class Test(models.Model, DateTimeMixin):
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=150)
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.title} - {self.is_open}"

    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"

<<<<<<< HEAD

class TestAccess(models.Model, DateTimeMixin):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    shared_with_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="shared_tests")

    def __str__(self):
        return f"{self.test} - {self.shared_with_teacher}"

    class Meta:
        verbose_name = "share with teacher"
        verbose_name_plural = "share with teachers"


class Article(models.Model, DateTimeMixin):
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"


class Question(models.Model, DateTimeMixin):
=======
class Question (models.Model, DateTimeMixin):
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    text = models.CharField(max_length=100)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    is_important = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.text} - {self.is_important}"

<<<<<<< HEAD
=======

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"


class Answer(models.Model, DateTimeMixin):
    text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.text} - {self.is_correct}"

    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"

<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class Attempt(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)

<<<<<<< HEAD
=======

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
    def __str__(self):
        return f"{self.pk} - {self.score}"

    class Meta:
        verbose_name = "attempt"
        verbose_name_plural = "attempts"
<<<<<<< HEAD


class Recommendation(models.Model):
    text = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    recommended_courses = models.ManyToManyField(Course, blank=True)
    recommended_articles = models.ManyToManyField(Article, blank=True)

    def __str__(self):
        return f"Recommendations for {self.student}"

    class Meta:
        verbose_name = "recommendation"
        verbose_name_plural = "recommendations"

    def generate_recommendations(self):
        incorrect_answers = self.test.answer_set.filter(is_correct=False)

        for answer in incorrect_answers:
            self.recommended_courses.add(answer.question.test.topic.course)
            self.recommended_articles.add(answer.question.test.topic.article_set.first())
=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
