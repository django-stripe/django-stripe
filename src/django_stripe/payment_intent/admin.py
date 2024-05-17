from django.contrib import admin

from django_stripe.common.admin import AbstractStripeAdmin

from .models import PaymentIntent


@admin.register(PaymentIntent)
class PaymentIntentAdmin(AbstractStripeAdmin):
    # Add any PaymentIntent-specific admin options here
    pass
