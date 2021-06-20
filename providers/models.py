from django.db import models


class Provider(models.Model):
    name = models.CharField("Наименование", max_length=255)

    class Meta:
        verbose_name = "поставщик"
        verbose_name_plural = "поставщики"

    def __str__(self):
        return self.name


class ProviderContact(models.Model):
    PHONE = 1
    EMAIL = 2
    CHOICES = [
        (PHONE, "телефон"),
        (EMAIL, "почта"),
    ]

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='contacts')
    contact_type = models.PositiveSmallIntegerField("Тип контакта", choices=CHOICES, default=PHONE)
    contact = models.CharField("Контакт", max_length=255)

    class Meta:
        verbose_name = "контакт поставщика"
        verbose_name_plural = "контакты поставщика"

    def __str__(self):
        return f"{self.get_contact_type_display()}: {self.contact}"


class ProviderAddress(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='addresses')
    address = models.CharField("Адрес", max_length=255)

    class Meta:
        verbose_name = "адрес поставщика"
        verbose_name_plural = "адреса поставщика"

    def __str__(self):
        return self.address
