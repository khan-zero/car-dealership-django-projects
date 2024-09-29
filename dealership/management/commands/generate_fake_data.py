from django.core.management.base import BaseCommand
from faker import Faker
from dealership.models import Vehicles, ClientsReviews

class Command(BaseCommand):
    help = 'Generate fake data for Vehicles and ClientsReviews models'

    def handle(self, *args, **kwargs):
        fake = Faker()

        def generate_fake_vehicles(num=10):
            for _ in range(num):
                Vehicles.objects.create(
                    year=str(fake.year()),
                    body=fake.word(),
                    manufactor=fake.company(),
                    condition=fake.random_element(elements=('brand new', 'quite new', 'used')),
                    model=fake.word(),
                    price=str(fake.random_int(min=10000, max=50000)),
                    kilometers=fake.random_int(min=10000, max=200000),
                    horse_power=fake.random_int(min=100, max=500),
                    transmission=fake.random_element(elements=('manual', 'automatic')),
                    img='path_to_default_image.jpg',
                    short_description=fake.sentence(),
                    long_description=fake.text()
                )

        def generate_fake_reviews(num=10):
            for _ in range(num):
                ClientsReviews.objects.create(
                    user_email=fake.email(),
                    full_name=fake.name(),
                    message=fake.text(),
                    location=fake.city()
                )

        generate_fake_vehicles(50)  # Generate 50 fake vehicles
        generate_fake_reviews(20)   # Generate 20 fake reviews
        self.stdout.write(self.style.SUCCESS('Successfully generated fake data'))
