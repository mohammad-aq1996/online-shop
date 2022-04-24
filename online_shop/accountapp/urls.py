from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


app_name = 'accountapp'
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login-view'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout-view'),
    path('register/', views.RegisterView.as_view(), name='register-view'),
    path('password/change/', views.PassChangeView.as_view(template_name='passChange.html'), name='pass-change'),
    path('password/change/done/',
         auth_view.PasswordChangeDoneView.as_view(template_name='passChaneDone.html'),
         name='pass-change-done'),

    path("password_reset/", views.PassResetView.as_view(template_name='passReset.html'), name="password_reset"),
    path(
        "password_reset/done/",
        auth_view.PasswordResetDoneView.as_view(template_name='passResetSent.html'),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PassResetConfirmView.as_view(template_name='passResetConf.html'),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_view.PasswordResetCompleteView.as_view(template_name='passResetDone.html'),
        name="password_reset_complete",
    ),

]
