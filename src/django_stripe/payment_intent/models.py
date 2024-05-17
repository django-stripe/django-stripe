from django_stripe.common.models import AbstractStripeModel


class PaymentIntent(AbstractStripeModel):
    """A model for storing Stripe PaymentIntent objects. Inherits all fields and methods from `AbstractStripeModel`."""

    pass
