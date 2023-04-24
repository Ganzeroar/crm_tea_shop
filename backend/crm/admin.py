from django.contrib import admin
from crm.models import Orders, OrderStatus, Clients, Products, ProductType, ProductUnit, City


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['status', 'product', 'client', 'quantity', 'date_of_creation']
    readonly_fields = ['product', 'client', 'quantity', 'date_of_creation']


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname','phone', 'city']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'unit', 'product_type']

admin.site.register(OrderStatus)

admin.site.register(ProductType)

admin.site.register(ProductUnit)

admin.site.register(City)
