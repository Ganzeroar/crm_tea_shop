from django.urls import path
from crm.api.products import OneProduct, SpecificProduct
from crm.api.orders import Orders, OneOrder
from crm.api.product_type import ProductType
from crm.api.clients import Clients
from crm.api.city import Cities

urlpatterns = [
    path('products', OneProduct.as_view()),
    path('products/<int:pk>', SpecificProduct.as_view()),
    path('product_type/<int:pk>', ProductType.as_view()),
    path('orders', Orders.as_view()),
    path('orders/<int:pk>', OneOrder.as_view()),
    path('clients', Clients.as_view()),
    path('cities', Cities.as_view()),
]
