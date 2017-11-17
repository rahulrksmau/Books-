# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render
from .forms import *
from .models import Book, Publisher, Author
from django.db.models import Q
from django.utils import timezone

# Create your views here.
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def index(request):
    books = Book.objects.all()

    author = Author.objects.all()
    aut_name = {}
    for book in books:
        names = []
        for item in book.author.all():
            names.append(item.name)
        names = set(names)
        aut_name[book.name] = names
    query = request.GET.get('q')
    if query:
        books = books.filter(Q(name__icontains=query)).distinct()
        authors = author.filter(Q(name__icontains=query)).distinct()
        return render(request, 'second/index.html', {'books': books, 'authors': authors})
    else:
        return render(request, 'second/index.html', {'books': books, 'aut_url': aut_name}, )


def register(request):
    form = Userform(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                book = Book.objects.filter(user=request.user)
                return render(request, 'second/index.html', {'book': book})
    return render(request, 'second/register.html', {'form': form})


def add_book(request):
    form = Bookform(request.POST or None, request.FILES or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.name = request.POST['name']
        book.price = request.POST['price']
        book.save()
        book.author = request.POST['author']
        book.publisher = Publisher.objects.get(pk=request.POST['publisher'])
        book.cover = request.FILES['cover']
        book.pubdate = request.POST['pubdate']
        cover_file = book.cover.url.split('.')[-1].lower()
        if cover_file not in IMAGE_FILE_TYPES:
            context = {
                'form': form,
                'error_message': "Image must be png or jpg or jpeg",
            }
            return render(request, 'second/add_book.html', context)
        book.save()
        authors = Author.objects.all()
        return render(request, 'second/index.html',
                      {'error_message': 'author data save successfully', 'authors': authors})
    return render(request, 'second/add_book.html', {'form': form})


def add_author(request):
    form = Authorform(request.POST or None, request.FILES or None)
    if form.is_valid():
        author = form.save(commit=False)
        author.name = request.POST['name']
        author.age = request.POST['age']
        author.pic = request.FILES['pic']
        file_type = author.pic.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'form': form,
                'error_message': "Image must be png or jpg or jpeg",
            }
            return render(request, 'second/add_author.html', context)
        author.save()
        authors = Author.objects.all()
        return render(request, 'second/author.html',
                      {'error_message': 'author data save successfully', 'authors': authors})
    return render(request, 'second/add_author.html', {'form': form})


def authors(request):
    authors = Author.objects.all()
    return render(request, 'second/author.html', {'authors': authors})


def publishers(request):
    pubs = Publisher.objects.all()
    return render(request, 'second/publishers.html', {'pubs': pubs})


def author_details(request, author):
    # print("author id =======" + str(author))
    author_profile = Author.objects.get(id=author)
    books = author_profile.book_set.all()
    return render(request, 'second/author_detail.html', {'author': author_profile, 'books': books})


def add_publisher(request):
    form = Publisherform(request.POST or None, request.FILES or None)
    if form.is_valid():
        pub = form.save(commit=False)
        pub.name = request.POST['name']
        pub.num_awards = request.POST['num_awards']
        pub.pic = request.FILES['pic']
        file_type = pub.pic.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'form': form,
                'error_message': "Image must be png or jpg or jpeg",
            }
            return render(request, 'second/add_publisher.html', context)
        pub.save()
        pubs = Publisher.objects.all()
        return render(request, 'second/publishers.html',
                      {'error_message': 'author data save successfully', 'pubs': pubs})
    return render(request, 'second/add_publisher.html', {'form': form})


def book_detail(request, bookId):
    book = Book.objects.get(id=bookId)
    comments = Comments.objects.filter(book_id=bookId)
    authors = [author for author in book.author.all()]
    form = Commentform(request.POST or None)
    if form.is_valid():
        c = form.save(commit=False)

    return render(request, 'second/book_detail.html',
                  {'book': book, 'authors': authors, 'comments': comments, 'form': form})


def pub_detail(request, pub_id):
    publisher = Publisher.objects.get(id=pub_id)
    books = Book.objects.filter(publisher_id=pub_id)
    return render(request, 'second/pub_detail.html', {'books': books, 'publisher': publisher})


def comment(request):
    # book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        user = request.POST['user']
        comment = request.POST['comment']
        book_id = request.POST['book_id']
        b = Book.objects.get(id=book_id)
        date = timezone.now()
        c = Comments(user=user, comment=comment, book=b, date=date)
        c.save()
        data = {"user": user, "comment": comment, "date": timezone.now().strftime("%B %d,%Y,%H:%M %p")}
        return JsonResponse(data)
    else:
        return render(request, 'second/index.html')

