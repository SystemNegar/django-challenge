from django.core.exceptions import ValidationError
from rest_framework import exceptions as rest_exceptions
from rest_framework.response import Response

from .errors import get_error_message


class ApiErrorsMixin:
    """
    Mixin that transforms Django and Python exceptions into rest_framework ones.
    without the mixin, they return 500 status code which is not desired.
    """

    expected_exceptions = {
        ValueError: rest_exceptions.ValidationError,
        ValidationError: rest_exceptions.ValidationError,
        PermissionError: rest_exceptions.PermissionDenied,
    }

    def handle_exception(self, exc):
        if isinstance(exc, tuple(self.expected_exceptions.keys())):
            drf_exception_class = self.expected_exceptions[exc.__class__]
            drf_exception = drf_exception_class(get_error_message(exc))

            return super().handle_exception(drf_exception)

        return super().handle_exception(exc)


class ApiResponseDetailMixin(Response):
    def __init__(self, data={}, status_message=None, message=None, status=None):
        data = {"data": data}
        if type(data) is dict:
            data["status_message"] = status_message
            data["message"] = message.replace(" ", "-")
        super().__init__(data=data, status=status)
