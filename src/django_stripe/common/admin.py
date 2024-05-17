from django.contrib import admin


class AbstractStripeAdmin(admin.ModelAdmin):
    list_display = ("stripe_id", "created_at", "updated_at")
    search_fields = ("stripe_id",)
    # Add any other common admin options here
    readonly_fields = ("stripe_id", "created_at", "updated_at", "data", "livemode", "connect_account_id")
