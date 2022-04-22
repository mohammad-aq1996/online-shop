from django.views.generic import CreateView
from .forms import UserCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView


class RegisterView(CreateView):
    """
        Signup view with the use of Django built-in signup view
        After signing up successfully user will automatically redirect to the login page
    """
    form_class = UserCreateForm
    success_url = reverse_lazy('accountapp:login-view')
    template_name = 'accountapp/register.html'


class PassChangeView(PasswordChangeView):
    success_url = reverse_lazy('accountapp:pass-change-done')