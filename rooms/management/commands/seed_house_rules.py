from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "This command creates house_rules "

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times",
    #         help="How many times do you want me tell you that I love you?",
    #     )

    def handle(self, *args, **options):
        house_rules = ["Pets allowed", "Smoking allowed"]
        for a in house_rules:
            HouseRule.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"{len(house_rules)} house_rule created"))
