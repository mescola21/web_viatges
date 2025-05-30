from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Importa les vistes pròpies de l'app accounts
from django.urls import path
from .views import flight_search

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),  # Ruta per al registre
    path('viatges_programats/', views.viatges_programats, name='viatges_programats'),
    path('profile/', views.perfil, name='profile'),
    path('viatges/', views.llista_viatges, name='viatges'),
    path('eliminar_viatge/<int:viatge_id>/', views.eliminar_viatge, name='eliminar_viatge'),
    path('reserva/<str:viatge_nom>/', views.reserva, name='reserva_viatge'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('staff/', views.staff, name='staff'),
    path('search-flights/', flight_search, name='flight_search'),
    path('editar-viatge/<int:viatge_id>/', views.editar_viatge, name='editar_viatge'),


]
