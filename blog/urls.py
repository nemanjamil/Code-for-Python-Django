from django.conf.urls import url, include
from django.views.generic import  ListView, DeleteView
from blog.models import Post
from blog.models import Vuktabela
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                template_name="blog/blog.html")),

    url('^vuk/$', views.vuk, name='vuk'),

    url('^vuktabela', ListView.as_view(
        queryset=Vuktabela.objects.all().order_by("first_name")[:14],
        template_name="blog/vuktabela.html"
    )),




]
