"""Module for handling Stripe webhooks."""

import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django_stripe.common.mapper import webhook_event_mapper
from django_stripe.common.models import AbstractStripeModel
from django_stripe.settings import django_stripe_settings


client = stripe.StripeClient(django_stripe_settings.STRIPE_API_KEY)


@csrf_exempt
def handle_stripe_webhook(request):
    """Handle Stripe webhook events."""
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)

    payload = request.body
    sig_header = request.headers.get("stripe-signature")

    try:
        event = client.construct_event(payload, sig_header, django_stripe_settings.STRIPE_WEBHOOK_SECRET)
        print(event)
    except ValueError as e:
        return HttpResponse(f"Error parsing payload: {str(e)}", status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(f"Error verifying webhook signature: {str(e)}", status=400)

    # Handle the event
    try:
        model_class: AbstractStripeModel = webhook_event_mapper.get(event.type)

        obj, created = model_class.objects.get_or_create(stripe_id=event.data.object.id)
        obj.process_data(event.data.object)
        return HttpResponse("Webhook processed successfully", status=200)
    except ValueError as e:
        print(e)
        return HttpResponse(str(e), status=404)  # Model class not found
    except Exception as e:
        return HttpResponse(f"Unhandled exception: {str(e)}", status=500)