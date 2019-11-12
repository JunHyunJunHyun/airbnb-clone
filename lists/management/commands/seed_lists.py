import random

from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten

from django_seed import Seed

from users import models as user_models
from rooms import models as room_models
from lists import models as list_models


NAME = "lists"


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
            list_models.List,
            number,
            {
                "name": lambda x: seeder.faker.sentence(),
                "user": lambda x: random.choice(users),
            },
        )

        created = seeder.execute()
        cleaned = flatten(list(created.values()))

        # for pk in cleaned:
        #     list_model = list_models.List.objects.get(pk=pk)

        #     for r in rooms:
        #         magic_number = random.randint(0, 15)

        #         if magic_number % 2 == 0 and magic_number % 7 == 0:
        #             list_model.rooms.add(r)

        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
