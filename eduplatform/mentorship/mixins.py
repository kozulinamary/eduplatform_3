from django.db import models

<<<<<<< HEAD

=======
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
class DateTimeMixin:
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
<<<<<<< HEAD
        abstract = True
=======
        abstract = True
>>>>>>> 5e6afde4c6d76c43252b22cb589861dd7611ff9a
