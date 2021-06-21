from django.db import models


class Order(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.SET_NULL, null=True, related_name='orders',
                               verbose_name="клиент")
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, related_name='orders',
                                verbose_name="товар")
    count = models.PositiveIntegerField("Количество товара", default=1)
    provider = models.ForeignKey('providers.Provider', on_delete=models.SET_NULL, null=True, related_name='orders',
                                 verbose_name="поставщик")
    created_at = models.DateTimeField("Дата и время заказа", auto_now_add=True)

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def __str__(self):
        return f"Заказ #{self.id}"

    def get_total_price(self):
        return self.product.retail_price * self.count

    get_total_price.short_description = "Сумма заказа"
