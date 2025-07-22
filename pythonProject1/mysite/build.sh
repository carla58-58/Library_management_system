#!/usr/bin/env bash
# Build script for Render

# Install dependencies
pip install -r requirements-production.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate
