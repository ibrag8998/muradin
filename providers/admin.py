from django.contrib import admin

from providers.models import Provider, ProviderContact, ProviderAddress


class ProviderContactInline(admin.TabularInline):
    model = ProviderContact
    extra = 0


class ProviderAddressInline(admin.TabularInline):
    model = ProviderAddress
    extra = 0


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    inlines = [ProviderContactInline, ProviderAddressInline]
