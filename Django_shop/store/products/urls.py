from django.urls import path
from products.views import product, test_context, basket_add, basket_delete

app_name = 'products'

urlpatterns = [
    path('', product, name='index'),
    path('<int:category_id>/', product, name='category'),
    path('page/<int:page>/', product, name='page'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-delete-add/<int:id>/', basket_delete, name='basket_delete'),
    path('test_context', test_context, name='test_context'),
]
