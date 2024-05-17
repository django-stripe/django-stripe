# src/django_stripe/checkout_session/tests/factories.py

from django_stripe.checkout_session.models import CheckoutSession
from django_stripe.common.tests.factories import AbstractStripeModelFactory


class CheckoutSessionFactory(AbstractStripeModelFactory):
    class Meta:
        model = CheckoutSession
