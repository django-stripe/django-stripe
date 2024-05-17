# src/django_stripe/charge/tests/test_models.py

from django.test import TestCase

from django_stripe.charge.models import Charge
from django_stripe.charge.tests.factories import ChargeFactory


class ChargeModelTest(TestCase):
    def test_create_charge(self):
        charge = ChargeFactory()
        self.assertIsInstance(charge, Charge)
        self.assertTrue(charge.stripe_id)
        self.assertTrue(charge.data)
