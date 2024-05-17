# Generated by Django 4.2.13 on 2024-05-17 04:11

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("payment_intent", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="paymentintent",
            name="connect_account_id",
            field=models.CharField(
                blank=True,
                help_text="The account_id that this object is on behalf of(Stripe Connect only",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="paymentintent",
            name="livemode",
            field=models.BooleanField(
                default=False, help_text="Whether the object was created in live mode or test mode"
            ),
        ),
    ]
