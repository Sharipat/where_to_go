from django.contrib import admin
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    raw_id_fields = ('place',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('place',
                    )
