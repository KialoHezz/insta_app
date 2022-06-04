from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('search_results/',views.search_results,name='search_results'),
    path('profile/',views.profile,name='profile'),

    path('login/',auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
]