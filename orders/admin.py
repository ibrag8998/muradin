from django.contrib import admin

from orders.models import Order, OrderProduct


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']
    list_display = ['get_products_str', 'get_total_count', 'get_total_price', 'created_at', 'get_address']
    inlines = [OrderProductInline]

    @admin.display(description="Адрес")
    def get_address(self, obj):
        return obj.client.addresses.first()

    @admin.display(description="Товары")
    def get_products_str(self, obj):
        if (order_product := obj.order_products.first()) is None:
            return None
        return f"{order_product.product.name}, ..."
