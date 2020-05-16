from django.contrib import admin
from django.urls import re_path,path
from . import views

app_name = 'characters'

urlpatterns = [
    re_path(r'^(?P<character_id>[0-9]+)/$',views.detail,name='detail'),
    re_path(r'^$', views.index, name='index'),

    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^all_char/$', views.all_char, name='all_char'),
    re_path(r'^all_books/$', views.all_books, name='all_books'),
    re_path(r'^all_movies/$', views.all_movies, name='all_movies'),
    re_path(r'^all_movies/(?P<movie_id>[0-9]+)/$', views.movie_detail, name='movie_detail'),
    re_path(r'^all_books/(?P<book_id>[0-9]+)/$', views.book_detail, name='book_detail'),
    re_path(r'^edit/(?P<user_id>[0-9]+)/$', views.edit, name='edit'),

]
