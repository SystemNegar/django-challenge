from .selectors import get_city_list


def city_list():
    try:
        cities = get_city_list()
        data = []
        for city in cities:
            data.append({"id": city.id, "name": city.name})
        return data
    except Exception:
        raise ValueError("City is empty")
