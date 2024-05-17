# src/django_stripe/payment_intent/tests/factories.py

from django_stripe.common.tests.factories import AbstractStripeModelFactory
from django_stripe.payment_intent.models import PaymentIntent


class PaymentIntentFactory(AbstractStripeModelFactory):
    class Meta:
        model = PaymentIntent
