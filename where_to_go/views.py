from django.shortcuts import render
from places.models import Place


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
                "detailsUrl": str(place.json_path)
            }
        },

        )

    return render(request, 'index.html', context={'place_json': place_json})


