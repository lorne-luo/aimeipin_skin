import logging
from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile
from stdimage import StdImageField
from stdimage.models import StdImageFieldFile


class PNGThumbnailStdImageFieldFile(StdImageFieldFile):
    # render a extra png thumbnail, PremiumProduct need png to generate pdf
    def render_variations(self, replace=False):
        for _, variation in self.field.variations.items():
            self.render_variation(self.name, variation, replace, self.storage)
            self.render_png_thumbnail(replace, variation)

    def render_png_thumbnail(self, replace, variation):
        if variation['name'] == 'thumbnail':
            original_thumbnail = self.get_variation_name(self.name, variation['name'])
            png_thumbnail = original_thumbnail + '.png'
            if replace:
                self.storage.delete(png_thumbnail)
            with self.storage.open(original_thumbnail) as f:
                with Image.open(f) as img:
                    with BytesIO() as file_buffer:
                        img.save(file_buffer, 'PNG')
                        f = ContentFile(file_buffer.getvalue())
                        self.storage.save(png_thumbnail, f)


class PNGThumbnailStdImageField(StdImageField):
    attr_class = PNGThumbnailStdImageFieldFile
