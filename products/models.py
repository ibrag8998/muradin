from django.db import models


class Product(models.Model):
    name = models.CharField("Наименование", max_length=255)
    count = models.PositiveIntegerField("Количество товара на складе", default=1)
    category = models.CharField("Категория товара", blank=True, max_length=255)
    arrival_date = models.DateField("Дата прибытия")
    cost_price = models.PositiveIntegerField("Закупочная стоимость")
    retail_price = models.PositiveIntegerField("Розничная цена")

    class Meta:
        verbose_name = "товар на складе"
        verbose_name_plural = "товары на складе"

    def __str__(self):
        return self.name
