from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'store_app'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('laptops/', views.LaptopListView.as_view(), name='laptop-view'),
    path('search/', views.SearchView.as_view(), name='search-view'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='detail-view'),
    path('purchases/', views.ShoppingListView.as_view(), name='purchases-view'),
    path('m/<int:pk>/', views.shopping_basket_minus, name='m-view'),
    path('p/<int:pk>/', views.shopping_basket_plus, name='p-view'),
    path('factor/', views.factor_view, name='factor'),
    path('bank/', TemplateView.as_view(template_name='store_app/bank.html'), name='bank'),
    path('uns/', TemplateView.as_view(template_name='store_app/unsuccess-result.html'), name='unsuccess'),
    path('success/', views.result_success_view, name='success'),
    path('mobiles/', views.MobileListView.as_view(), name='mobile-view'),
]
