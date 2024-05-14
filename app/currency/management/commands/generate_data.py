import random

from currency.models import ContactUS, Rate

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = "Generate random records" # noqa

    def handle(self, *args, **options):
        banks = ['monobank', 'privatbank', 'vkurse', 'raiffeisenbank']
        currency_types = ['usd', 'uer', 'gbp']
        fake = Faker()

        for i in range(100):
            Rate.objects.create(
                currency_type=random.choice(currency_types),
                sale='{:.2f}'.format(round(random.uniform(38, 40), 2)),
                buy='{:.2f}'.format(round(random.uniform(39, 41), 2)),
                source=random.choice(banks),
                )

            ContactUS.objects.create(
                email_from=fake.free_email(),
                subject=fake.sentence(),
                message=fake.text(200),
                )
