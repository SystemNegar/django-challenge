from .models import City


def get_city_list():
    return City.objects.all()
