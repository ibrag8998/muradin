from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'count', 'get_total_price', 'get_address']

    @admin.display(description="Адрес")
    def get_address(self, obj):
        return obj.client.addresses.first()
