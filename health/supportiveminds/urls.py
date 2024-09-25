from django.urls import path
from .views import home_view, resources, mood_tracker, resources_view, register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('resources/', resources, name='resources'),
    path('mood_tracker/', mood_tracker, name='mood_tracker'),
    path('ideas/', resources_view, name='ideas' ),
]