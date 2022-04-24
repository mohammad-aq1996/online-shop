from django.urls import path, include
from .views import *
urlpatterns = [
    path('laptop/list/', LaptopListAPIView.as_view()),
    path('mobile/list/', MobileListAPIView.as_view()),
    path('product/detail/<int:pk>/', ProductRetrieveUpdateDeleteAPIView.as_view()),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/',
         PassResetConfirmView.as_view(),
         name='password_reset_confirm')
]