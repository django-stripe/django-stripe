"""Module for URL routing for the Django Stripe app."""

from django.urls import path

from django_stripe.webhooks import handle_stripe_webhook


urlpatterns = [
    path("webhook/", handle_stripe_webhook, name="stripe-webhook"),
]
