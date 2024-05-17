from django.contrib import admin

from django_stripe.checkout_session.models import CheckoutSession
from django_stripe.common.admin import AbstractStripeAdmin


@admin.register(CheckoutSession)
class CheckoutSessionAdmin(AbstractStripeAdmin):
    # Add any CheckoutSession-specific admin options here, or leave as is for common settings
    pass
