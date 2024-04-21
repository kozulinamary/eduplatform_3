from django.contrib import admin
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
from .models import Course, Topic, Article, Test, Question, Answer, Attempt

>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Attempt)
<<<<<<< HEAD
admin.site.register(Recommendation)
admin.site.register(TestAccess)
=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
