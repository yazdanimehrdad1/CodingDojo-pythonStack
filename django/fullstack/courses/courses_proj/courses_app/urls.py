from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('create', views.create),
    path('courses/destroy/<int:course_id>', views.destroy),
    path('remove/<int:course_id>', views.remove)
]
