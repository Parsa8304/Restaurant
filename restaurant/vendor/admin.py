from django.contrib import admin
from .models import Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_name', 'user', 'is_approved', 'created_at', 'modified_at')
    list_display_links = ('user', 'vendor_name')
    search_fields = ('vendor_name',)
    list_filter = ('is_approved',)
    ordering = ('-created_at',)


admin.site.register(Vendor)