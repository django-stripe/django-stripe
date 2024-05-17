# src/django_stripe/session/admin.py
from django.contrib import admin

from django_stripe.common.admin import AbstractStripeAdmin

from .models import Charge


@admin.register(Charge)
class SessionAdmin(AbstractStripeAdmin):
    # Add any Charge-specific admin options here, or leave as is for common settings
    pass
