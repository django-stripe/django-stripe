from django.conf import settings


class DjangoStripeSettings:
    def __init__(self):
        """Settings for the Stripe API Key and Webhook Secret."""
        self.STRIPE_API_KEY = getattr(settings, "STRIPE_API_KEY", "my_fake_key")
        self.STRIPE_WEBHOOK_SECRET = getattr(settings, "STRIPE_WEBHOOK_SECRET", "default_value")


django_stripe_settings = DjangoStripeSettings()
