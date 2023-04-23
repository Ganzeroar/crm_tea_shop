from django.urls import path
from crm.api.products import OneProduct, SpecificProduct
from crm.api.orders import Orders
from crm.api.product_type import ProductType


urlpatterns = [
    path('products', OneProduct.as_view()),
    path('products/<int:pk>', SpecificProduct.as_view()),
    path('product_type/<int:pk>', ProductType.as_view()),
    path('orders', Orders.as_view()),
]
