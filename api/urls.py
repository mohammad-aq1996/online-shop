from django.urls import path
from .views import *
urlpatterns = [
    path('laptop/list/', LaptopListAPIView.as_view()),
    path('mobile/list/', MobileListAPIView.as_view()),
    path('product/detail/<int:pk>/', ProductRetrieveUpdateDeleteAPIView.as_view()),
]