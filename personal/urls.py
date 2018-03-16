from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # r'^$'
    url(r'^contact/', views.contact, name='contact'),

]
