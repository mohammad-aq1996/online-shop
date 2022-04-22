from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


app_name = 'account'
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login-view'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout-view'),
    path('register/', views.RegisterView.as_view(), name='register-view'),
    path('password/change/', views.PassChangeView.as_view(template_name='passChange.html'), name='pass-change'),
    path('password/change/done/',
         auth_view.PasswordChangeDoneView.as_view(template_name='passChaneDone.html'),
         name='pass-change-done'),
]
