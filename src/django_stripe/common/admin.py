from django.contrib import admin
from django.contrib import messages


class AbstractStripeAdmin(admin.ModelAdmin):
    list_display = ("stripe_id", "created_at", "updated_at")
    search_fields = ("stripe_id",)
    # Add any other common admin options here
    readonly_fields = ("stripe_id", "created_at", "updated_at", "data", "livemode", "connect_account_id")

    actions = ["sync_stripe_account_object"]

    def sync_stripe_account_object(self, request, queryset):
        for obj in queryset:
            try:
                obj.retrieve_data_from_stripe()
                self.message_user(request, f"Successfully synced {obj.stripe_id}", messages.SUCCESS)
            except Exception as e:
                self.message_user(request, f"Error syncing {obj.stripe_id}: {str(e)}", messages.ERROR)
