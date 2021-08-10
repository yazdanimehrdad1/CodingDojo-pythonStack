# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('', views.main),
    path('wall', views.wall),
    path('logout', views.logout),
    path('create_message', views.create_message),
    path('create_comment/<int:message_id>', views.create_comment),
    
]
