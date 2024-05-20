from django_stripe.common.models import AbstractStripeModel


class PaymentIntent(AbstractStripeModel):
    """A model for storing Stripe PaymentIntent objects. Inherits all fields and methods from `AbstractStripeModel`."""

    stripe_sdk_name = "payment_intents"

    class Meta:
        app_label = "payment_intent"
