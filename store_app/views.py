from django.shortcuts import render
from .forms import UserCreateForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Product


class RegisterView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('store_app:login-view')
    template_name = 'register.html'


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'store_app/product-list.html'


class SearchView(ProductListView):
    def get_queryset(self):
        search = self.request.GET.get('search')
        products = Product.objects.filter(title__icontains=search)
        return products













