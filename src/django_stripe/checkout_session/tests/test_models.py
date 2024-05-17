# src/django_stripe/checkout_session/tests/test_models.py

from django.test import TestCase

from django_stripe.checkout_session.models import CheckoutSession
from django_stripe.checkout_session.tests.factories import CheckoutSessionFactory


class CheckoutSessionModelTest(TestCase):
    def test_create_checkout_session(self):
        checkout_session = CheckoutSessionFactory()
        self.assertIsInstance(checkout_session, CheckoutSession)
        self.assertTrue(checkout_session.stripe_id)
        self.assertTrue(checkout_session.data)
