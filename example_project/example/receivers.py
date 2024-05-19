# users_app/signals.py

from django.dispatch import receiver

from django_stripe.signals import get_signal


webhook_signal = get_signal("charge.succeeded")


@receiver(webhook_signal)
def handle_stripe_event(sender, **kwargs):
    instance = kwargs.get("instance")
    event_type = kwargs.get("type")
    print(f"Received {event_type} for {instance.stripe_id}")
    print("Yaay! I can now handle the event")
    # User can add their custom handling logic here


pi_succeeded = get_signal("payment_intent.succeeded")


@receiver(pi_succeeded)
def handle_payment_intent_succeeded(sender, **kwargs):
    instance = kwargs.get("instance")
    event_type = kwargs.get("type")
    print(f"Received {event_type} for {instance.stripe_id}")
    print("Yaay! I can now handle the event")
    # User can add their custom handling logic here
