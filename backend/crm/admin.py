from django.contrib import admin
from django.urls import reverse
from django.template.defaultfilters import escape

from crm.models import (City, Clients, Orders, OrderStatus, Products,
                        ProductType, ProductUnit, ProductOrder)


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ['id', 'client_name_surname', 'client_city', 'date_of_creation', 'total_cost']
    
    list_display = ['date_of_creation', 'client_name_surname', 'client_phone', 'order_number', 'status']

    # fields = ['id', 'client', 'client_phone', 'status', 'client_city', 'destination_address', 'product', 'total_cost']
    fields = ['client', 'status', 'destination_address', 'product']

    def client_name_surname(self, obj):
        return f'{obj.client.surname} {obj.client.name}'
    client_name_surname.short_description = 'Фамилия и имя клиента' 

    def client_phone(self, obj):
        return obj.client.phone
    client_phone.short_description = 'Номер телефона'

    def client_city(self, obj):
        return obj.client.city
    client_city.short_description = 'Город'

    def order_number(self, obj):
        return obj.id
    order_number.short_description = 'Номер заказа'

    def total_cost(self, obj):
        return obj.product.price * obj.quantity
    total_cost.short_description = 'Сумма заказа'

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname','phone', 'city']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'unit', 'product_type']

admin.site.register(ProductOrder)

admin.site.register(OrderStatus)

admin.site.register(ProductType)

admin.site.register(ProductUnit)

admin.site.register(City)
