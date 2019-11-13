import random
from datetime import timedelta, datetime

from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django.utils import timezone

from django_seed import Seed

from users import models as user_models
from rooms import models as room_models
from reservations import models as reservation_models


NAME = "reservations"


class Command(BaseCommand):
    help = f"This Command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help=f"How many {NAME} do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "check_in": lambda x: timezone.now().date(),
                "check_out": lambda x: timezone.now().date()
                + timedelta(days=random.randint(3, 25)),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )

        seeder.execute()
        print(timezone.now().date())
        print(datetime.now())
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
