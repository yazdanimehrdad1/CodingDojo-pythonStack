from django.urls import path 
from . import views


urlpatterns = [

    path('', views.index),
    # path('<str:first_name>', views.function_one),
    path('<int:test_number>/edit/<str:test_string>', views.edit),
    path('show', views.show)
]
