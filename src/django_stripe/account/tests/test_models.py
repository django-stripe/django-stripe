# src/django_stripe/account/tests/test_models.py

from django.test import TestCase

from django_stripe.account.models import Account
from django_stripe.account.tests.factories import AccountFactory


class AccountModelTest(TestCase):
    def test_create_account(self):
        account = AccountFactory()
        self.assertIsInstance(account, Account)
        self.assertTrue(account.stripe_id)
        self.assertTrue(account.data)
