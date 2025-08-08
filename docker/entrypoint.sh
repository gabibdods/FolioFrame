#!/usr/bin/env bash
set -e

if [ -n "$POSTGRES_HOST" ] && [ -n "$POSTGRES_PORT" ]; then
    until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
        sleep 0.5
    done
fi

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"