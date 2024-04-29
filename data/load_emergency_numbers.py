import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PFA.settings')
django.setup()


import csv
from django.core.management.base import BaseCommand
from interface.models import EmergencyNumber

class Command(BaseCommand):
    help = 'Load emergency numbers from CSV file into the database'

    def handle(self, *args, **kwargs):
        file_path = "emergency_numbers.csv"  # Update with your CSV file path
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                EmergencyNumber.objects.create(
                    country=row['country'],
                    emergency_number=row['emergency_number']
                )
        print("Emergency numbers loaded successfully")
        self.stdout.write(self.style.SUCCESS('Emergency numbers loaded successfully'))
