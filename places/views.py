from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from .models import Place, Image


def show_places(request):
    places = Place.objects.all()

    place_json = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in places:
        place_json["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "detailsUrl": f'../{str(place.json_path)}'
            }
        },

        )

    return render(request, 'index.html', context={'place_json': place_json})


def place_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_images = place.images.all()
    image_url = [place_image.image.url for place_image in place_images]
    json_response = {
        "title": place.title,
        "imgs": image_url,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.latitude,
            "lng": place.longitude
        }
    }
    return JsonResponse(json_response, json_dumps_params={"ensure_ascii": False, 'indent': 4}, safe=False)
