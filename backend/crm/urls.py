from django.urls import path
from crm.api.products import OneProduct, SpecificProduct

urlpatterns = [
    path('products', OneProduct.as_view()),
    path('products/<int:pk>', SpecificProduct.as_view()),

]
