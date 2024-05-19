# Handling Stripe Webhook Events with Django Signals

This section of the documentation explains how to set up Django signal receivers to handle events from Stripe webhooks. By following these instructions, you can customize your application's response to different Stripe events.

## Overview

When Stripe triggers a webhook event, our application sends a corresponding Django signal. You can connect to these signals with receivers to perform custom logic based on the event data.

## Step-by-Step Guide

### 1. Import the Signal

First, you need to import the `get_signal` function from our signal module. This function allows you to retrieve or create a signal for a specific Stripe event type.

```python
from django_stripe.signals import get_signal
```

### 2. Define Your Signal Receiver

A signal receiver is a function that gets called when a specific signal is sent. Use the `@receiver` decorator from Django to link your function to a Stripe event signal. Here's how you can define a receiver for the `charge.succeeded` event:

```python
from django.dispatch import receiver
from django_stripe.signals import get_signal

# Retrieve the signal for the 'charge.succeeded' event
charge_succeeded_signal = get_signal("charge.succeeded")

@receiver(charge_succeeded_signal)
def handle_charge_succeeded(sender, **kwargs):
    instance = kwargs.get("instance")
    event_type = kwargs.get("type")
    print(f"Received {event_type} for {instance.stripe_id}")
    # Add your custom logic here
```

### 3. Connect More Receivers

You can connect receivers to as many Stripe event types as needed by repeating the steps above. For example, to handle a `payment_intent.succeeded` event:

```python
pi_succeeded_signal = get_signal("payment_intent.succeeded")

@receiver(pi_succeeded_signal)
def handle_payment_intent_succeeded(sender, **kwargs):
    instance = kwargs.get("instance")
    event_type = kwargs.get("type")
    print(f"Received {event_type} for {instance.stripe_id}")
    # Add your custom logic here
```

### 4. Ensure Signal Receivers Are Loaded

Make sure that your signal receivers are loaded when your Django app starts. You typically do this in the `AppConfig` of your application. Add your receivers module to the app configuration as follows:

```python
from django.apps import AppConfig

class ExampleConfig(AppConfig):
    name = 'example_project.example'
    def ready(self):
        import example_project.example.receivers  # noqa
```

This setup ensures that your signal receivers are connected when the Django app is ready, allowing them to listen and respond to Stripe webhook events.
