from django.shortcuts import render
from .forms import UserCreateForm, CommentForm
from django.views.generic import CreateView, ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Product, ShoppingBasket, Comment
from django.shortcuts import redirect


class RegisterView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('store_app:login-view')
    template_name = 'register.html'


class LaptopListView(ListView):
    model = Product
    queryset = model.objects.filter(category__slug__exact='laptop').order_by('-created_at')
    context_object_name = 'products'
    template_name = 'store_app/product-list.html'
    paginate_by = 3


class MobileListView(ListView):
    model = Product
    queryset = model.objects.filter(category__slug__exact='mobile').order_by('-created_at')
    context_object_name = 'products'
    template_name = 'store_app/mobile-list.html'
    paginate_by = 3


class ProductListAvailableView(LaptopListView):
    queryset = Product.objects.filter(category__slug__exact='laptop', available__exact=True)


class ProductListCheapestView(LaptopListView):
    queryset = Product.objects.filter(category__slug__exact='laptop', available__exact=True).order_by('price')


class ProductListExpensiveView(LaptopListView):
    queryset = Product.objects.filter(category__slug__exact='laptop', available__exact=True).order_by('-price')


class MobileListAvailableView(MobileListView):
    queryset = Product.objects.filter(category__slug__exact='mobile', available__exact=True)


class MobileListCheapestView(MobileListView):
    queryset = Product.objects.filter(category__slug__exact='mobile', available__exact=True).order_by('price')


class MobileListExpensiveView(MobileListView):
    queryset = Product.objects.filter(category__slug__exact='mobile', available__exact=True).order_by('-price')


class SearchView(LaptopListView):
    paginate_by = 0

    def get_queryset(self):
        search = self.request.GET.get('search')
        products = Product.objects.filter(title__icontains=search)
        return products


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'store_app/products-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        context['comments'] = Comment.objects.filter(product_id=self.kwargs['pk'], status__exact='publish')
        return context

    def post(self, request, **kwargs):
        if 'count' in request.POST:
            print(request.POST)
            product = Product.objects.get(id=self.kwargs['pk'])
            number = request.POST.get('count')
            product.buy(number)
            product.save()
            if ShoppingBasket.objects.filter(product=product, buyyer=request.user).exists():
                t = ShoppingBasket.objects.get(product=product)
                t.count = t.count + int(number)
                t.save()
            else:
                ShoppingBasket.objects.create(product=product, buyyer=request.user, count=number)
            return redirect('store_app:purchases-view')

        if 'subject' in request.POST:
            print(request.POST)
            form = CommentForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                user = request.user
                product = self.model.objects.get(id=self.kwargs['pk'])
                comment = Comment(product=product, user=user, subject=subject, message=message)
                comment.save()
            return redirect('store_app:detail-view', self.kwargs['pk'])


class ShoppingListView(LoginRequiredMixin, ListView):
    model = ShoppingBasket
    template_name = 'store_app/shopping-list.html'
    context_object_name = 'purchases'

    def get_queryset(self):
        return self.model.objects.filter(buyyer=self.request.user)


def shopping_basket_minus(req, pk):
    purchase = ShoppingBasket.objects.get(id=pk)
    current_product = Product.objects.get(id=purchase.product.id)
    if purchase.count > 1:
        purchase.count = purchase.count - 1
        purchase.save()

    else:
        purchase.delete()
    current_product.count_add()
    current_product.save()
    return redirect('store_app:purchases-view')


def shopping_basket_plus(req, pk):
    purchase = ShoppingBasket.objects.get(id=pk)
    current_product = Product.objects.get(id=purchase.product.id)
    if current_product.count > 0:
        purchase.count = purchase.count + 1
        purchase.save()
        current_product.count_minus()
        current_product.save()
    return redirect('store_app:purchases-view')


def factor_view(req):
    purchases = ShoppingBasket.objects.filter(buyyer=req.user)
    total = 0
    for purchase in purchases:
        total += purchase.product.price * purchase.count
    return render(req, 'store_app/factor.html', {'purchases': purchases, 'total_price': total})


def result_success_view(req):
    purchases = ShoppingBasket.objects.filter(buyyer=req.user)
    purchases.delete()
    return render(req, 'store_app/success-result.html')






