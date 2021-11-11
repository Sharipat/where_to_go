from urllib.parse import urlparse

import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('serialized_place', nargs='+', type=str)

    def handle(self, *args, **options):
        for place_link in options['serialized_place']:
            json_response = requests.get(place_link.strip())
            json_response.raise_for_status()
            place_raw = json_response.json()
            place, created = Place.objects.get_or_create(
                title=place_raw['title'],
                defaults={
                    'title': place_raw['title'],
                    "description_short": place_raw['description_short'],
                    "description_long": place_raw['description_long'],
                    "longitude": place_raw['coordinates']['lng'],
                    "latitude": place_raw['coordinates']['lat'],

                })
            for image_link in place_raw['imgs']:
                image_name = urlparse(image_link).path.split('/')[-1]
                image_response = ContentFile(requests.get(image_link).content)
                place_image, created = Image.objects.get_or_create(place_id=place.id, image=image_name)
                place_image.image.save(image_name, image_response, save=True)
