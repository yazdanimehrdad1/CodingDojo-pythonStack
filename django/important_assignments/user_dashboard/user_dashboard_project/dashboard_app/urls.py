from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.landing),
    path('login', views.login),
    path('login_user', views.login_user),
    path('register', views.register),
    path('register_user', views.register_user),
    path('dashboard', views.dashboard),
    path('users/show/<int:user_id>', views.show_user),

    path('user/process_message/<int:user_id>', views.submit_message),
    path('admin_delete_user/<int:user_id>', views.admin_delte_user),
]
