"""politiquiz development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = (b'\x98\x0b\xaaNE\xeb\xe5i\x87\xf5\x08\\?L\xfd\xeb\x86<I\x86'
              b'\x1a\x8cu\xb4')
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
politiquiz_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = politiquiz_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/politiquiz.sqlite3
DATABASE_FILENAME = politiquiz_ROOT/'var'/'politiquiz.sqlite3'
