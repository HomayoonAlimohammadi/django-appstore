#!/bin/sh

# Optionally, wait for the database to be ready.
# For example, you can use 'wait-for-it' or a simple loop:
# while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
#   echo "Waiting for PostgreSQL..."
#   sleep 1
# done

echo "Running migrations..."
python manage.py migrate --noinput

# Optionally, collect static files if needed:
# python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn django_appstore_project.wsgi:application --bind 0.0.0.0:8000

