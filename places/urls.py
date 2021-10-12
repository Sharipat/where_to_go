from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from .views import show_places, place_view

urlpatterns = [path('', show_places),
               path('<int:place_id>/', place_view)

               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
