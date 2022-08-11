#!/bin/sh

service=$1
shift

while ! nc -z db 3306 ; do
    echo "$service service waiting for the MySQL Server..."
    sleep 3
done

echo "MySQL Server available for $service service"

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

exec "$@"