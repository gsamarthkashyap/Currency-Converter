"""
Django settings for currency_converter project.
...
"""

import os # <-- ADDED
import dj_database_url # <-- ADDED
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# 1. SECURITY WARNING: Use Environment Variables for Production!
# The SECRET_KEY is loaded from an environment variable for security.
# If not found, it defaults to the insecure one (development fallback).
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-3aewfh##^558qo#w^s5d54_=kl3$mq-@04p%@j^f#cjs#p5ggw')

# 2. SECURITY WARNING: Turn DEBUG OFF in production!
# DEBUG is controlled by an environment variable. Render will set this to False.
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# 3. Security: ALLOWED_HOSTS must include your Render URL.
# It's loaded from an environment variable (comma-separated list).
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'converter',
    'corsheaders',
]

MIDDLEWARE = [
    # 4. WhiteNoise must be placed directly after SecurityMiddleware
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <-- ADDED
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'currency_converter.urls'
# ... (TEMPLATES and WSGI_APPLICATION sections remain the same) ...


# Database
# 5. Production Database Configuration (PostgreSQL/Render)
# Uses dj_database_url to parse the DATABASE_URL environment variable from Render
if not DEBUG:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600  # Persistent connection for performance
        )
    }
else:
    # Use SQLite in development when DEBUG is True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ... (Password validation and Internationalization sections remain the same) ...


# Static files (CSS, JavaScript, Images)
# 6. Static File Configuration for Production
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # <-- ADDED (Required by collectstatic)

# Default primary key field type
# ...

# 7. CORS Settings (Make sure your frontend URL is allowed for production)
CORS_ALLOW_ALL_ORIGINS = True 
# For production, it's safer to use CORS_ALLOWED_ORIGINS = ['https://your-frontend-url.onrender.com']