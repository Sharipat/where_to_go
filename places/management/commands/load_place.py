import logging
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place

logger = logging.getLogger('load_place')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.debug('debug information')


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('serialized_place', nargs='+', type=str)

    def handle(self, *args, **options):
        for place_link in options['serialized_place']:
            json_response = requests.get(place_link.strip())
            try:
                json_response.raise_for_status()
            except requests.exceptions.HTTPError:
                logging.error(f'Ошибка подлкючения {json_response.status_code}')
            except 'error' in json_response:
                logging.error('Ошибка подключения')
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
                image_response = requests.get(image_link)
                try:
                    image_response.raise_for_status()
                except requests.exceptions.HTTPError:
                    logging.error(f'Ошибка подлкючения {image_response.status_code}')
                except 'error' in image_response:
                    logging.error('Ошибка подключения')
                image_content = ContentFile(image_response.content)
                place_image, created = Image.objects.get_or_create(place_id=place.id, image=image_name)
                place_image.image.save(image_name, image_content, save=True)
