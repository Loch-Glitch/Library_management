from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adminsignup/', views.admin_signup, name='adminsignup'),
    path('usersignup/', views.user_signup, name='usersignup'),
    path('userlogin/', views.user_login, name='userlogin'),
    path('selection/',views.selection_page,name='selection'),
    path('userselection/',views.user_selection,name='userselection'),
]
