from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name = 'store_app'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html')),
]