from django.urls import path
from .views import Home, CategoryCreate, CategoryUpdate, CategoryDelete, CategoryDetail, PostList, PostCreate, PostDelete, PostUpdate
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from dash import views
from .views import (postemail)
from .views import (categoryemail)


app_name = 'dash'
urlpatterns = [
     path('', Home.as_view(), name ='Home'),
     url(r'^post/(?P<pk>[\d]+)/update/$', postemail, name='post_update'),

     url(r'^login/$', auth_views.LoginView.as_view(template_name='dash/login.html'), name='login'),
     url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
     url(r'^category/add/$', views.CategoryCreate.as_view(), name='category_add'),
     url(r'^category/(?P<pk>[\d]+)/delete/$', views.CategoryDelete.as_view(), name='category_delete'),
     url(r'^category/(?P<pk>[\d]+)/$', views.CategoryDetail.as_view(), name='category_detail'),
     path('postlist/<int:pk>', views.PostList.as_view(), name='post_list'),
     url(r'^post/add/$', views.PostCreate.as_view(), name='post_add'),
     url(r'^post/(?P<pk>[\d]+)/delete/$', views.PostDelete.as_view(), name='post_delete'),
     path('post/<int:pk>', postemail, name='post_update'),
     path('category/<int:pk>', categoryemail, name='category_update'),






    
]