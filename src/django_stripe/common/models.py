"""Abstract model for storing Stripe objects."""

import json

import stripe
from django.db import models

from django_stripe.app_settings import get_setting


client: stripe.StripeClient = stripe.StripeClient(get_setting.STRIPE_API_KEY)


class AbstractStripeModel(models.Model):
    """An abstract base class for storing Stripe-related objects in the database.

    This model provides a standardized schema for storing information from Stripe
    objects, including their unique identifier, mode, data, and timestamps.
    It is intended to be inherited by other models which interact with various
    Stripe objects such as charges, payments, or accounts.

    Attributes:
        stripe_id (:class:`django.db.models.CharField`): Unique identifier for the Stripe object.
        livemode (:class:`django.db.models.BooleanField`): Indicates whether the object was created within Stripe's live mode.
        data (:class:`django.db.models.JSONField`): Stores the complete JSON representation of the Stripe object.
        created_at (:class:`django.db.models.DateTimeField`): Timestamp indicating when the object was first created.
        updated_at (:class:`django.db.models.DateTimeField`): Timestamp indicating when the object was last updated.
        connect_account_id (:class:`django.db.models.CharField`): The Stripe Connect account ID this object is associated with, if any. # noqa B950



    The class is abstract and should not be instantiated directly.
    """

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
        """Returns a string representation of the model, showing the class name and the Stripe object ID."""
        return f"{self.__class__.__name__} - {self.stripe_id}"

    def process_data(self, event: stripe.Event) -> None:
        """Updates the model's data based on a Stripe webhook payload.

        This method is designed to handle the data from a webhook event, updating
        the model's fields accordingly.

        Args:
            event (stripe.Event): The Stripe event object containing the webhook data.

        No return value; the instance is updated and saved to the database.
        """
        data = event.data.object
        self.livemode = event.livemode
        account = getattr(event, "account", None)
        if account:
            self.connect_account_id = event.account
        self.data = data
        self.save()

    def retrieve_data_from_stripe(self) -> json:
        """Retrieves the latest data from Stripe for a specific object ID and updates the model.

        This method directly interacts with the Stripe API to fetch the latest data for
        a specific object, updating the model's data field and saving the changes.

        Raises:
            ValueError: If `stripe_sdk_name` is not defined in the subclass.



        Returns:
            json: The JSON data retrieved from the Stripe API as a dictionary.
        """
        if not hasattr(self, "stripe_sdk_name"):
            raise ValueError("stripe_sdk_name must be defined in the subclass.")
        api_resource = getattr(client, self.stripe_sdk_name)
        response = api_resource.retrieve(self.stripe_id)
        self.data = response
        self.save()
        return response
