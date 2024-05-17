import factory
from django.utils import timezone

from django_stripe.common.models import AbstractStripeModel


class AbstractStripeModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractStripeModel
        abstract = True

    stripe_id = factory.Sequence(lambda n: f"stripe_id_{n}")
    livemode = factory.Faker("boolean")
    data = factory.Faker("json")
    created_at = factory.LazyFunction(timezone.now)
    updated_at = factory.LazyFunction(timezone.now)
    connect_account_id = factory.Faker("uuid4")
