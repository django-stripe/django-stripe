from django.contrib import admin

from django_stripe.common.admin import AbstractStripeAdmin

from .models import Account


@admin.register(Account)
class AccountAdmin(AbstractStripeAdmin):
    # Add any Account-specific admin options here
    pass
