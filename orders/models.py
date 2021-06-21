from django.db import models


class Order(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.SET_NULL, null=True, related_name='orders',
                               verbose_name="клиент")
    # product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, related_name='orders',
    #                             verbose_name="товар")
    # count = models.PositiveIntegerField("Количество товара", default=1)
    provider = models.ForeignKey('providers.Provider', on_delete=models.SET_NULL, null=True, related_name='orders',
                                 verbose_name="поставщик")
    created_at = models.DateTimeField("Дата и время заказа", auto_now_add=True)

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def __str__(self):
        return f"Заказ #{self.id}"

    def get_total_price(self):
        return sum(order_product.product.retail_price * order_product.count for order_product in
                   self.order_products.all())

    get_total_price.short_description = "Сумма заказа"

    def get_total_count(self):
        return self.order_products.aggregate(total_count=models.Sum('count'))['total_count']

    get_total_count.short_description = "Итого единиц товара"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products', verbose_name="Заказ")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_products',
                                verbose_name="Товар")
    count = models.PositiveIntegerField("Количество товара", default=1)

    class Meta:
        verbose_name = "товар из заказа"
        verbose_name_plural = "товары из заказа"

    def __str__(self):
        return f"{self.product.name} x{self.count} из заказа #{self.order.id}"
