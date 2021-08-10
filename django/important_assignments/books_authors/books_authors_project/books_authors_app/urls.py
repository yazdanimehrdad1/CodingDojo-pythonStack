from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.main),
    path('books', views.show_books),
    path('books/create', views.create_book),
    path('books/<int:book_id>', views.show_book),
    path('books/<int:book_id>/assign', views.assign_book),

    path('authors', views.show_authors),
    path('authors/create', views.create_author),
    path('authors/<int:author_id>', views.show_author),
    path('authors/<int:author_id>/assign', views.assign_author),

]
