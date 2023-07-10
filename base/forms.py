from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User
from .models import Student
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from django.contrib.auth.models import Permission

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(UserCreationForm):
    username = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.username.lower()
        if commit:
            user.save()
            student = Student.objects.create(user=user, username=user.username)
            permission = Permission.objects.get(codename='add_room_abdalla')
            print(permission)
            # user.user_permissions.add(permission)
            user.save()
            student.save()
        return user

