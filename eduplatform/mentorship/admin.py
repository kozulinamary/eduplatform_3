from django.contrib import admin

from .models import Group, Message, Student, Teacher, User

admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Message)