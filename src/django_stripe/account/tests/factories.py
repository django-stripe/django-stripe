# src/django_stripe/account/tests/factories.py

from django_stripe.account.models import Account
from django_stripe.common.tests.factories import AbstractStripeModelFactory


class AccountFactory(AbstractStripeModelFactory):
    class Meta:
        model = Account
