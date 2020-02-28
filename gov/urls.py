from django.urls import path
from .views import CourseList, CourseCategory, Gallery
from . import views 
from .views import Home
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import (searchposts)
from .views import (contact_us)


app_name = 'govlink'
urlpatterns = [
     path('', Home.as_view(), name ='Home'),
     url(r'^category/$', views.CourseCategory.as_view(), name ='CourseCategory'),
     url(r'^gallery/$', views.gallery.as_view(), name ='gallery'),
     path('coursedetail/<int:pk>/', views.coursedetail.as_view(), name = 'coursedetail'),
     path('courselist/<int:pk>', views.CourseList.as_view(), name = 'courselist'),
     url(r'^search/$', searchposts, name='searchposts'),
     url(r'^contact/$', contact_us, name='contact'),
     
     #path('post/add/', views.Post_create, name='PostCreate'),
    ]
