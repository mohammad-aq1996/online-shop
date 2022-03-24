from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_view

app_name = 'store_app'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login-view'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout-view'),

]