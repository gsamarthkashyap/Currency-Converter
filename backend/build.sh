#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status.
set -o errexit

# 1. Install Python dependencies from requirements.txt
# This ensures all necessary packages (like Django, Gunicorn, WhiteNoise, etc.) are installed.
echo "Installing Python dependencies..."
pip install -r requirements.txt

# 2. Collect static files
# This gathers all static assets (CSS, JS, images) into the STATIC_ROOT directory.
echo "Collecting static files..."
python manage.py collectstatic --no-input

# 3. Apply database migrations
# This creates or updates your database tables based on your Django models.
echo "Applying database migrations..."
python manage.py migrate

# Optional: Create a superuser on first deploy (use environment variables for credentials in production!)
# echo "Creating superuser (if it doesn't exist)..."
# python manage.py createsuperuser --noinput || true