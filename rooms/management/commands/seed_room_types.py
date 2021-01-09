from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = "This command creates house_rules "

    def handle(self, *args, **options):
        room_types = ["Entire place", "Private Room", "Hotel Room", "Shared Room"]
        for a in room_types:
            RoomType.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"{len(room_types)} room_type created"))
