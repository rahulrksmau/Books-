# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    pic = models.FileField(default='')

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300)
    genre = models.CharField(max_length=50, default='Fantcy')
    pages = models.PositiveIntegerField(default=500)
    price = models.PositiveIntegerField()
    rating = models.FloatField(default=3.6)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey('Publisher')
    pubdate = models.DateField(null=True)
    cover = models.FileField(default='')
    book_file = models.FileField(default='')

    def __unicode__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()
    pic = models.FileField(default='')

    def __unicode__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()
    country = models.CharField(default='America', max_length=100)
    pic = models.FileField(default='')

    def __unicode__(self):
        return self.name


class Comments(models.Model):
    user = models.CharField(primary_key=True, max_length=50)
    comment = models.TextField(default='', max_length=200)
    book = models.ForeignKey(Book)
    date = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.user

    
class ExtendUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user',
    )
    written_book = models.ManyToManyField(Book)

    def __unicode__(self):
        return self.user.name