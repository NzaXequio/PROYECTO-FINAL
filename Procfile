web: python manage.py runserver 0.0.0.0:$PORT --noreload
web: python manage.py collectstatic --no-input; gunicorn myapp.wsgi --log-file - --log-level debug