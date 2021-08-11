from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.landing),
    path('login', views.login),
    path('register', views.register),
]
