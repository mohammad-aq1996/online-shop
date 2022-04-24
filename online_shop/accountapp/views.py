from django.views.generic import CreateView
from .forms import UserCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView


class RegisterView(CreateView):
    """
        Signup view with the use of Django built-in signup view
        After signing up successfully user will automatically redirect to the login page
    """
    form_class = UserCreateForm
    success_url = reverse_lazy('accountapp:login-view')
    template_name = 'register.html'


class PassChangeView(PasswordChangeView):
    """
        because of using separate app, We should add our successfully url
    """
    success_url = reverse_lazy('accountapp:pass-change-done')


class PassResetView(PasswordResetView):
    """
        because of using separate app, We should add our email_template_name successfully url
    """
    email_template_name = 'passResetEmail.html'
    success_url = reverse_lazy('accountapp:password_reset_done')


class PassResetConfirmView(PasswordResetConfirmView):
    """
        because of using separate app, We should add our successfully url
    """
    success_url = reverse_lazy('accountapp:password_reset_complete')




