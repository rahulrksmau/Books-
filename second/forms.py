from django import forms
from django.contrib.auth.models import User

from .models import *


class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'genre', 'price', 'author', 'publisher', 'cover', 'pubdate']


class Authorform(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'age', 'pic']


class Publisherform(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'num_awards', 'pic']


class Commentform(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['user', 'comment']
