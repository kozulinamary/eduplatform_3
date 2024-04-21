from django.contrib import admin

from .models import User, Group, Message, Student, Teacher


admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Message)

