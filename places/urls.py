from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import place_view, show_places

urlpatterns = [path('', show_places, name='index'),
               path('<int:place_id>/', place_view, name='place_show_url')

               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
