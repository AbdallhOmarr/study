from django.contrib import admin

# Register your models here.
from . models import Room, Topic, Message, Student, Staff

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Student)
admin.site.register(Staff)