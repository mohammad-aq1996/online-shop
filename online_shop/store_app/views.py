from django.shortcuts import render
from .forms import CommentForm
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, ShoppingBasket, Comment
from django.shortcuts import redirect


class ProductListView(ListView):
    """
        Base class for product views
        On every page user will see 12 objects of products list
    """
    model = Product
    context_object_name = 'products'
    template_name = 'store_app/product-list.html'
    paginate_by = 12


class LaptopListView(ProductListView):
    """
        This class inherit from ProductListView class
        It returns laptop products descending
    """
    queryset = Product.objects.filter(category__slug__exact='laptop').order_by('-created_at')


class MobileListView(ProductListView):
    """
        This class inherit from ProductListView class
        It returns mobile products descending
    """
    queryset = Product.objects.filter(category__slug__exact='mobile').order_by('-created_at')


class SearchView(LaptopListView):
    """
        This page inherits from 'LaptopListView' class
        Get information about search box and return posts whose titles contain search box information
        Also, there is no pagination and all posts appear on one page
    """
    paginate_by = 0

    def get_queryset(self):
        search = self.request.GET.get('search')
        products = Product.objects.filter(title__icontains=search)
        return products


class ProductDetailView(DetailView):
    """
        Details about a particular product
        Logged in users can add product to their shopping basket and leave a comment about the product
    """
    model = Product
    context_object_name = 'product'
    template_name = 'store_app/products-detail.html'

    def get_context_data(self, **kwargs):
        """
            It returns comment form and published comments for specific product
        """
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        context['comments'] = Comment.objects.filter(product_id=self.kwargs['pk'], status__exact='publish')
        return context

    def post(self, request, **kwargs):
        """
            The user specifies the number of products and clicks on the 'Buy' button, the product will add to the user's
            shopping basket and the number of that product will be reduced from the database. If a product exists in
            the shopping basket and the user decide to click again on the buy button it will add to the number of
            that product in the user's shopping basket
        """
        if 'count' in request.POST:
            product = Product.objects.get(id=self.kwargs['pk'])
            number = request.POST.get('count')
            product.buy(number)
            product.save()
            if ShoppingBasket.objects.filter(product=product, buyer=request.user).exists():
                t = ShoppingBasket.objects.get(product=product)
                t.count = t.count + int(number)
                t.save()
            else:
                ShoppingBasket.objects.create(product=product, buyer=request.user, count=number)
            return redirect('store_app:purchases-view')

        if 'subject' in request.POST:
            # If user submit a comment, and if it was valid, it will save in database
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
    """
        For access to this view user must be logged in
        This class return user's purchases list
    """
    model = ShoppingBasket
    template_name = 'store_app/shopping-list.html'
    context_object_name = 'purchases'

    def get_queryset(self):
        return self.model.objects.filter(buyer=self.request.user)


def shopping_basket_minus(req, pk):
    """
        After a particular user added a product to her/him shopping basket, he/she can reduce or increase the number of
        that product on her/him shopping basket. When a user decides to reduce the number of specific products on
        her/him shopping basket, He / She click on the '-' link. After clicking on '-', this function will be called.
        This function reduces the number of that specific product in the shopping basket. Then the number of that
        specific product in the database will be increased.
        If a user has one specific product of products he/she will see 'delete' link instead of '-' link.After clicking
        on 'delete', the specific product will be removed from the shopping basket, and increase number of that product
        in the database
    """
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
    """
        After a particular user added a product to her/him shopping basket, he/she can reduce or increase the number of
        that product on her/him shopping basket. When a user decides to increase the number of specific products on
        her/him shopping basket, He / She click on the '+' link. After clicking on '+', this function will be called.
        This function increases the number of that specific product in the shopping basket. Then the number of that
        specific product in the database will be reduces.
    """
    purchase = ShoppingBasket.objects.get(id=pk)
    current_product = Product.objects.get(id=purchase.product.id)
    if current_product.count > 0:
        purchase.count = purchase.count + 1
        purchase.save()
        current_product.count_minus()
        current_product.save()
    return redirect('store_app:purchases-view')


def factor_view(req):
    """
        It returns specific user purchases and total price of shopping
    """
    purchases = ShoppingBasket.objects.filter(buyer=req.user)
    total = 0
    for purchase in purchases:
        total += purchase.product.price * purchase.count
    return render(req, 'store_app/factor.html', {'purchases': purchases, 'total_price': total})


def result_success_view(req):
    """
        If bank transaction being successful this function will call
        It deleted specific user shopping basket
    """
    purchases = ShoppingBasket.objects.filter(buyer=req.user)
    purchases.delete()
    return render(req, 'store_app/success-result.html')






