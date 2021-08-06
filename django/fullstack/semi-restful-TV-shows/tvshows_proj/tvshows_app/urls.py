# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('shows', views.shows),
    path('add_show', views.add_show),
    path('create', views.create),
    path('shows/<int:show_id>' , views.show ),
    path('shows/<int:show_id>/edit', views.edit ),
    path('shows/<int:show_id>/delete', views.delete),
    path('shows/<int:show_id>/update', views.update )
]



