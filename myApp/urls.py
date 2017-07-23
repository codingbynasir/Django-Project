from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^category/(?P<cat_id>[0-9]+)$', views.single_category, name="single_cat"),
    url(r'^(?P<books_id>[0-9]+)$', views.book, name="book"),
    url(r'^cat', views.category, name="category"),
    url(r'^login', views.login, name="login"),
]
