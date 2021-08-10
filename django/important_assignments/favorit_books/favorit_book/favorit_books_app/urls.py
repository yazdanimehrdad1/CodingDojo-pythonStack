# from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('register', views.register),
    path('books', views.books),
    path('login', views.login),
    path('logout', views.logout),
    path('books/create_book', views.create_book),
    path('books/<int:book_id>', views.show_book),
    # path('books/<int:book_id>/add_favorit' , views.add_favorit)
    path('books/<int:book_id>/update', views.update),
    path('books/<int:book_id>/delete', views.delete),
    path('unfavorite/<int:book_id>',views.unfavorit),
    path('favorite/<int:book_id>',views.favorit),
    
    
]