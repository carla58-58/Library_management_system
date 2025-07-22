import os
import dj_database_url
from decouple import config
from .settings import *

# Production settings
DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY', default='django-insecure-pqzewr@g%ybvpgib5^%sx@y%&z13^wvtr^pt^+294-0@2ye)p^')

# Allowed hosts for production
ALLOWED_HOSTS = [
    '127.0.0.1', 
    'localhost', 
    '.vercel.app', 
    '.now.sh',
    '.railway.app',
    '.render.com',
    '.herokuapp.com',
    '.pythonanywhere.com',
    'library-management-system.onrender.com',  # Replace with your actual Render URL
    '*'  # Allow all hosts for initial deployment (remove in production)
]

# Database configuration for production
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    # Fallback to SQLite for local development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Additional Vercel-specific settings
ALLOWED_HOSTS.extend([
    '.vercel.app',
    'your-project-name.vercel.app'  # Replace with your actual Vercel URL
])

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# WhiteNoise for serving static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security settings for production
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
