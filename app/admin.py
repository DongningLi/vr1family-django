from django.contrib import admin
from .models import DonorInformation
from .models import Category
from .models import Page
from .models import RecipientInformation
from .models import RecipientFamilyMember
from .models import AidKit
from .models import AidKitItem
from .models import AidItem
from .models import AidItemRequest
from .models import RequestItem
from .models import RequestKit
from .models import Donation
from .models import Inventory


@admin.register(DonorInformation)
class DonorInformationAdmin(admin.ModelAdmin):
    search_fields = ('full_name',)
    list_display = ('full_name', 'email', 'id')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'baseline_quantity', 'stock_remaining')


@admin.register(AidItem)
class AidItemAdmin(admin.ModelAdmin):
    search_fields = ('item_name', 'id')
    list_display = ('item_name', 'item_baseline_quantity', 'stock_remaining')


admin.site.register(Page)


class AidKitItemInline(admin.TabularInline):
    model = AidKitItem
    extra = 1


@admin.register(AidKit)
class AidKitAdmin(admin.ModelAdmin):
    inlines = [AidKitItemInline]
    search_fields = ('kit_name',)


class RequestItemInline(admin.TabularInline):
    model = RequestItem
    extra = 1
    autocomplete_fields = ('item',)


class RequestKitInline(admin.TabularInline):
    model = RequestKit
    extra = 1
    autocomplete_fields = ('kit',)


@admin.register(AidItemRequest)
class AidItemRequestAdmin(admin.ModelAdmin):
    inlines = [RequestItemInline, RequestKitInline]
    autocomplete_fields = ('recipient',)
    list_display = ('request_id', 'recipient', 'request_fulfilled', 'created_at')


class RecipientFamilyMemberInline(admin.StackedInline):
    model = RecipientFamilyMember
    extra = 1


@admin.register(RecipientInformation)
class RecipientInformationAdmin(admin.ModelAdmin):
    inlines = [RecipientFamilyMemberInline]
    search_fields = ('full_name', 'email')


class InventoryInline(admin.TabularInline):
    model = Inventory
    autocomplete_fields = ('item',)


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    inlines = [InventoryInline]
    autocomplete_fields = ('donor',)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass
