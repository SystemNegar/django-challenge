from .selectors import get_all_city


def city_list():
    try:
        cities = get_all_city()
        data = []
        for city in cities:
            data.append({"id": city.id, "name": city.name})
        return data
    except Exception:
        raise ValueError("City list is empty")
