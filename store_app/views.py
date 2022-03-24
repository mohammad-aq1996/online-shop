from django.shortcuts import render
from .forms import UserCreateForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class RegisterView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('store_app:login-view')
    template_name = 'register.html'
