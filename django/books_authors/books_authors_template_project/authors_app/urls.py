from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('books/<int:book_id>', views.show_book ),
    path('authors/<int:author_id>', views.show_author ),
    


]   