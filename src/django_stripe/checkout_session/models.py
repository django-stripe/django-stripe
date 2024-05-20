from django_stripe.common.models import AbstractStripeModel


class CheckoutSession(AbstractStripeModel):
    """A model for storing Stripe CheckoutSession objects. Inherits all fields and methods from `AbstractStripeModel`."""

    stripe_sdk_name = "checkout.sessions"

    class Meta:
        app_label = "checkout_session"
