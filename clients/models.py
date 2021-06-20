from django.db import models


class Client(models.Model):
    full_name = models.CharField("ФИО", max_length=255)

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"

    def __str__(self):
        return self.full_name


class ClientContact(models.Model):
    PHONE = 1
    EMAIL = 2
    CHOICES = [
        (PHONE, "телефон"),
        (EMAIL, "почта"),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contacts')
    contact_type = models.PositiveSmallIntegerField("Тип контакта", choices=CHOICES, default=PHONE)
    contact = models.CharField("Контакт", max_length=255)

    class Meta:
        verbose_name = "контакт клиента"
        verbose_name_plural = "контакты клиента"

    def __str__(self):
        return f"{self.get_contact_type_display()}: {self.contact}"


class ClientAddress(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='addresses')
    address = models.CharField("Адрес", max_length=255)

    class Meta:
        verbose_name = "адрес клиента"
        verbose_name_plural = "адреса клиента"

    def __str__(self):
        return self.address
