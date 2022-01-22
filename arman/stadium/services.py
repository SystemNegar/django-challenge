from .models import Stadium


def create_stadium(**validate_data):
    try:
        Stadium.objects.create(**validate_data)
    except Exception:
        raise ValueError("can't create stadium with given fields")
