import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists.models import List
from rooms.models import Room
from users.models import User


class Command(BaseCommand):
    help = "This command creates many lists"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many lists do you want create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = User.objects.all()
        seeder.add_entity(
            List,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "user": lambda x: random.choice(all_users),
            },
        )

        created_lists = seeder.execute()
        created_clean = flatten(list(created_lists.values()))
        all_rooms = Room.objects.all()
        for pk in created_clean:
            list_ = List.objects.get(pk=pk)
            to_add = all_rooms[random.randint(0, 5) : random.randint(6, 30)]
            # 모든 room들중 랜덤으로 받아서 queryset형태로 리턴
            list_.rooms.add(*to_add)
            # *to_add 한이유는 to_add는 배열형태의 queryset이기때문에
            # 나는 배열안에 요소를 얻기를 원하기때문에

        self.stdout.write(self.style.SUCCESS(f"{number} lists Created!"))