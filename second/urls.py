from django.conf.urls import url
# from django.contrib import admin
from . import views

apps_name = 'first'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    # url(r'^login/', views.login, name='login'),
    #  url(r'^logout', views.logout, name='logout'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^add_author/$', views.add_author, name='add_author'),
    url(r'^authors/$', views.authors, name='authors'),
    url(r'^publishers/$', views.publishers, name='publishers'),
    url(r'^author_details/(?P<author>[0-9]+)/$', views.author_details, name='author_details'),
    url(r'^book_details/(?P<bookId>[0-9]+)/$', views.book_detail, name='book_detail'),
    url(r'^publisher_details/(?P<pub_id>[0-9]+)/$', views.pub_detail, name='pub_detail'),
    url(r'^adding publisher/$', views.add_publisher, name='add_publisher'),
    url(r'^comment/$', views.comment, name='comment'),
 #   url(r'^book/(?P<book_name>[a-zA-Z]*)/$', views.book, name='book'),
]

