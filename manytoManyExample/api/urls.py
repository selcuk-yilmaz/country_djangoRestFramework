from django.urls import path
from manytoManyExample.api import views as api_views

urlpatterns = [
    path('customers/',api_views.CustomersListCreateAPIView.as_view(), name='customers-listesi'),
    path('products/',api_views.ProductsListCreateAPIView.as_view(), name='products-listesi'),
    path('orders/',api_views.OrdersListCreateAPIView.as_view(), name='orders-listesi')
]


# urlpatterns = [
#     path('makaleler/',api_views.makale_list_create_api_view, name='makale-listesi'),
#     path('makaleler/<int:pk>', api_views.makale_detail_api_view, name='makale-detay'),
# ]