# src/django_stripe/payment_intent/tests/test_models.py

from django.test import TestCase

from django_stripe.payment_intent.models import PaymentIntent
from django_stripe.payment_intent.tests.factories import PaymentIntentFactory


class PaymentIntentModelTest(TestCase):
    def test_create_payment_intent(self):
        payment_intent = PaymentIntentFactory()
        self.assertIsInstance(payment_intent, PaymentIntent)
        self.assertTrue(payment_intent.stripe_id)
        self.assertTrue(payment_intent.data)
