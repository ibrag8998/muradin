from django.contrib import admin
from django.utils import timezone

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'category', 'arrival_date', 'get_storage_time', 'cost_price', 'retail_price']

    @admin.display(description="Дней на складе")
    def get_storage_time(self, obj):
        return (timezone.now().date() - obj.arrival_date).days
