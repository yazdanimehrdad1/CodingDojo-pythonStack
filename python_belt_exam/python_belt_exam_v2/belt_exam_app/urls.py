from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),


    path('render_login', views.render_login),
    path('render_register', views.render_register),# add to the render_login.html



    path('register', views.register_user),
    path('login', views.login_user),
    path('logout', views.logout),
    path('main', views.main),
]