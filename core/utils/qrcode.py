import os

from MyQR import myqr
from django.conf import settings


def generate_qrcode(url, uuid):
    dest_dir = os.path.join(settings.MEDIA_ROOT, settings.QRCODE_FOLDER)
    file_name = '%s.png' % uuid
    version, level, qr_name = myqr.run(
        url,
        version=1,
        level='H',
        picture=None,
        colorized=False,
        contrast=1.0,
        brightness=1.0,
        save_name=file_name,
        save_dir=dest_dir
    )
    return '%s%s/%s' % (settings.MEDIA_URL, settings.QRCODE_FOLDER, file_name)
