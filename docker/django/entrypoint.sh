#!/bin/sh 

#python manage.py makemigrations accounts orders
#python manage.py migrate

#python manage.py collectstatic --noinput 
gunicorn drf_oms.wsgi -b $GUNICORN_BIND_IP:$GUNICORN_BIND_PORT --workers $GUNICORN_WORKERS --threads $GUNICORN_THREADS --log-file - --log-level=$GUNICORN_LOG_LEVEL --timeout $GUNICORN_TIMEOUT --access-logfile -
