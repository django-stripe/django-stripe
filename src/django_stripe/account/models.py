from django_stripe.common.models import AbstractStripeModel


class Account(AbstractStripeModel):
    """A model for storing Stripe Account objects. Inherits all fields and methods from `AbstractStripeModel`."""

    stripe_sdk_name = "accounts"
