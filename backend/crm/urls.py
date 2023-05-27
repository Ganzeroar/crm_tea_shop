from django.urls import path
from crm.api.products import OneProduct, SpecificProduct, ProductsOfTypes
from crm.api.orders import Orders, OneOrder, ProductOrderView
from crm.api.product_type import ProductTypeView, ProductTypesView
from crm.api.clients import Clients
from crm.api.city import Cities
from crm.api.order_statuses import OrderStatusesView
from crm.api.unit import UnitView
from crm.api.phone_validator import PhoneValidator

urlpatterns = [
    path('products', OneProduct.as_view()),
    path('products/<int:pk>', SpecificProduct.as_view()),
    path('products_of_type/<int:pk>', ProductsOfTypes.as_view()),
    path('create_products', ProductOrderView.as_view()),
    path('product_types', ProductTypesView.as_view()),
    path('product_type/<int:pk>', ProductTypeView.as_view()),
    path('orders', Orders.as_view()),
    path('orders/<int:pk>', OneOrder.as_view()),
    path('order_statuses/<int:pk>', OrderStatusesView.as_view()),
    path('clients', Clients.as_view(), name='clients'),
    path('cities', Cities.as_view()),
    path('unit/<int:pk>', UnitView.as_view()),
    path('phone/<str:phone>', PhoneValidator.as_view()),
]
