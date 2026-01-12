#!/bin/sh
set -e

echo "Waiting for PostgreSQL to be ready..."
while ! nc -z $DB_HOST 5432; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done
echo "PostgreSQL is up - continuing..."

# マイグレーション
echo "Running migrations..."
python manage.py migrate --noinput

# collectstatic
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Gunicorn or runserver
echo "Starting server..."
exec gunicorn backend.wsgi:application --bind 0.0.0.0:8000
