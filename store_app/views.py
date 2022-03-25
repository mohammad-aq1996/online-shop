from django.shortcuts import render
from .forms import UserCreateForm
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Product, ShoppingBasket
from django.shortcuts import redirect


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


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'store_app/products-detail.html'

    def post(self, request, **kwargs):
        product = Product.objects.get(id=self.kwargs['pk'])
        number = request.POST.get('count')
        product.buy(number)
        product.save()
        if ShoppingBasket.objects.filter(product=product).exists():
            t = ShoppingBasket.objects.get(product=product)
            t.count = t.count + int(number)
            t.save()
        else:
            ShoppingBasket.objects.create(product=product, buyyer=request.user, count=number)

        return redirect('store_app:product-view')











