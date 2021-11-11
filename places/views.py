from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def show_places(request):
    places = Place.objects.all()

    serialized_place = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in places:
        serialized_place["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "detailsUrl": reverse('place_show_url', args=[place.id])
            }
        },

        )

    return render(request, 'index.html', context={'serialized_place': serialized_place})


def place_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_images = place.images.all()
    image_url = [place_image.image.url for place_image in place_images]
    context = {
        "title": place.title,
        "imgs": image_url,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude,
        }
    }
    return JsonResponse(context, json_dumps_params={"ensure_ascii": False, 'indent': 4}, safe=False)
