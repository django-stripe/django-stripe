"""App configuration."""

from django.apps import AppConfig


class DjangoStripeConfig(AppConfig):
    """App configuration for django-stripe."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "django_stripe"
