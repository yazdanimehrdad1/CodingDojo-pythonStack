from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.authors),

    path('books/<int:book_id>', views.show_book ),
    path('books/<int:book_id>/assign', views.assign_author),
    path('remove_author/<int:author_id>/<int:book_id>', views.remove_author),

    path('authors/<int:author_id>', views.show_author ),
    path('authors/<int:author_id>/assign', views.assign_book),



]   