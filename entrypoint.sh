#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Creating admin user..."
python manage.py createsuperuser --noinput \
  --username raguna \
  --email pasupoto17@gmail.com || true

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
exec gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
