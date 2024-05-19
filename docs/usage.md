# django-stripe Installation and Configuration

This document provides instructions for installing and configuring django-stripe in your Django project.

## Installation

Install django-stripe using pip:

```bash
pip install django-stripe
```

## Configuration

### Add to `INSTALLED_APPS`

Include the necessary django-stripe submodules in your `settings.py`. Only add the modules you need:

```python
INSTALLED_APPS = [
    "django_stripe.checkout_session",
    "django_stripe.payment_intent",
    "django_stripe.account",
    "django_stripe.charge",
]
```

### Configure API Key and Webhook Secret

In your `settings.py`, set your Stripe API key and webhook secret:

```python
STRIPE_API_KEY = 'your_stripe_api_key_here'
STRIPE_WEBHOOK_SECRET = 'your_stripe_webhook_secret_here'
```

Replace `'your_stripe_api_key_here'` and `'your_stripe_webhook_secret_here'` with your actual credentials.

### Setup Stripe Webhook Endpoint

Configure a webhook in your Stripe dashboard to point to:

```
https://yourdomain.com/stripe/webhook/
```

## Synchronization

Once configured, django-stripe will synchronize Stripe objects (like charges, payment intents, etc.) to your database, based on the modules included in your `INSTALLED_APPS`.
