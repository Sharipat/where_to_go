from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from .views import show_places, place_view

urlpatterns = [path('', show_places, name='place'),
               path('<int:place_id>/', place_view, name='place_show_url')

               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
