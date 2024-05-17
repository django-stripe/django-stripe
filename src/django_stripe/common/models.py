"""Abstract model for storing Stripe objects."""

import json

import stripe
from django.db import models

from django_stripe.app_settings import get_setting


client: stripe.StripeClient = stripe.StripeClient(get_setting.STRIPE_API_KEY)


class AbstractStripeModel(models.Model):
    """Abstract model for storing Stripe objects."""

    stripe_id = models.CharField(max_length=255, unique=True, help_text="Unique identifier for the Stripe object")
    livemode = models.BooleanField(default=False, help_text="Whether the object was created in live mode or test mode")
    data = models.JSONField(default=dict, help_text="Full JSON data from the Stripe object")
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="The time when the object was first created in the database"
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="The time when the object was last updated in the database"
    )
    connect_account_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="The account_id that this object is on behalf of(Stripe Connect only",
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.__class__.__name__} - {self.stripe_id}"

    def process_data(self, event: stripe.Event) -> None:
        """Update the model's data from Stripe webhook payload."""
        data = event.data.object
        self.livemode = event.livemode
        self.connect_account_id = event.account
        self.data = data
        self.save()

    def retrieve_data_from_stripe(self, id: str) -> json:
        """Retrieve the latest data from the Stripe API."""
        class_name = self.__class__.__name__.lower()
        api_method = getattr(client, class_name).retrieve
        self.data = api_method(id)
        self.save()
        return self.data
