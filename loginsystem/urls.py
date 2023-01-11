from django.urls import path
from django.contrib.auth import views as auth_views
from loginsystem import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='loginsystem/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='loginsystem/logout.html'), name='logout'),
]
