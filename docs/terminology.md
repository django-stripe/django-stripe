# Terminology and Definitions

## Stripe Webhook

a webhook is a way for an app to provide other applications with real-time information. A webhook delivers data to other applications as it happens, meaning you get data immediately. Unlike typical APIs where you would need to poll for data very frequently in order to get it real-time. This makes webhooks much more efficient for both provider and consumer. The only drawback to webhooks is the difficulty of initially setting them up.
django-stripe uses webhooks to listen for events from Stripe. When an event is received, django-stripe will trigger the appropriate signal, which you can listen for in your own code.

## Topic 2

Content
