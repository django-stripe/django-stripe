from django_stripe.common.models import AbstractStripeModel


class Charge(AbstractStripeModel):
    """A model for storing Stripe Charge objects. Inherits all fields and methods from `AbstractStripeModel`."""

    pass
