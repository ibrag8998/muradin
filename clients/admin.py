from django.contrib import admin

from clients.models import Client, ClientContact, ClientAddress


class ClientContactInline(admin.TabularInline):
    model = ClientContact
    extra = 0


class ClientAddressInline(admin.TabularInline):
    model = ClientAddress
    extra = 0


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [ClientContactInline, ClientAddressInline]
