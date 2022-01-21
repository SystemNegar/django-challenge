from .models import City


def get_all_city():
    return City.objects.all()
