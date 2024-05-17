# src/django_stripe/charge/tests/factories.py

from django_stripe.charge.models import Charge
from django_stripe.common.tests.factories import AbstractStripeModelFactory


class ChargeFactory(AbstractStripeModelFactory):
    class Meta:
        model = Charge
