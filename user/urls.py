from django.urls import path
from .forms import LoginForm
from user import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',
         auth_views.LoginView.as_view(template_name='user/login.html', authentication_form=LoginForm),
         name='login'),
    path('home/', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')
]
