from django.contrib import admin
from .models import Fundraiser

@admin.register(Fundraiser)
class FundraiserAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "target_amount", "raised_amount", "approved", "created_at")
    list_filter = ("approved", "created_at")
    search_fields = ("title", "description")
    actions = ["approve_fundraisers"]

    def approve_fundraisers(self, request, queryset):
        queryset.update(approved=True)
    approve_fundraisers.short_description = "Approve selected fundraisers"
