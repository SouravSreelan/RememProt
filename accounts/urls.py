from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from . forms import UserLoginForm

app_name = 'users'

urlpatterns = [
path('register/', views.account_register, name='register'),
path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html',
                                                form_class=UserLoginForm), name='login'),

path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

]
