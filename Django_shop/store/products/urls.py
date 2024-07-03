from django.urls import path
from products.views import product, test_context

app_name = 'products'

urlpatterns = [
    path('', product, name='index'),
    path('test_context', test_context, name='test_context'),
]
