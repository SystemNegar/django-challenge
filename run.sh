#!/bin/sh
docker exec -it django-challenge_web_1 python manage.py makemigrations 
docker exec -it django-challenge_web_1 python manage.py migrate
docker exec -it django-challenge_web_1 ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
