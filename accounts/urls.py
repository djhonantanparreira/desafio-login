from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('menu/', views.menu, name='menu'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]