from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'accountapp'
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='accountapp/login.html'), name='login-view'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout-view'),
    path('register/', views.RegisterView.as_view(), name='register-view'),
]
