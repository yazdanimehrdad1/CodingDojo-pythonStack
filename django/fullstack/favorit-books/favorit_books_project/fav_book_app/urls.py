from django.urls import path 
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('register', views.register),
    path('books',views.show_all ),
    path('login', views.login),
    path('create', views.create),
    path('books/<int:book_id>', views.show_one),
    path('books/favorit/<int:book_id>', views.favorit),
    path('logout', views.logout)
]
