from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Place


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
    place_title = get_object_or_404(Place, pk=place_id)

    return HttpResponse(str(place_title))
