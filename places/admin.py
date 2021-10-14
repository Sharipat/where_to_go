from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ['image_preview']
    fields = ('image', 'image_preview', 'order')


    def image_preview(self, place):
        return format_html('<img src="{}" height=200px />', place.image.url)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place',)
