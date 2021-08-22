from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register_user),
    path('login', views.login_user),
    # path('users/<int:user_id>', views.single_user),
    path('logout', views.logout),
    path('main', views.main),
    path('add_trip')
]