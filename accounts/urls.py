from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Importa les vistes pròpies de l'app accounts
from .views import viatges_programats

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),  # Ruta per al registre
    path('viatges_programats/', viatges_programats, name='viatges_programats'),
]
