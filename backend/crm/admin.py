from django.contrib import admin
import requests
from crm.models import (City, Clients, Orders, OrderStatus, Products,
                        ProductType, ProductUnit, ProductOrder, NotificationInfo)


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ['id', 'client_name_surname', 'client_city', 'date_of_creation', 'total_cost', 'client']

    list_display = ['date_of_creation', 'client_name_surname', 'client_phone', 'order_number', 'status']

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

    def get_object(self, request, object_id, s):
        self.obj = super(OrderAdmin, self).get_object(request, object_id)
        return self.obj

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "product":
            kwargs["queryset"] = ProductOrder.objects.filter(orders=self.obj)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        url = 'http://127.0.0.1:8080/status_was_updated'
        data = {'status': str(obj.status), 'telegram_user_id': str(obj.client.telegram_user_id)}
        requests.post(url=url, json=data)
        super().save_model(request, obj, form, change)


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'city']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'unit', 'product_type']


admin.site.register(NotificationInfo)

admin.site.register(OrderStatus)

admin.site.register(ProductType)

admin.site.register(ProductUnit)

admin.site.register(City)
