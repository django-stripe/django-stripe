"""App configuration."""

from django.apps import AppConfig


app_name = "django_stripe"


class DjangoStripeConfig(AppConfig):
    """App configuration for django-stripe."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "django_stripe"
