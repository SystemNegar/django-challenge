from django.core.exceptions import ValidationError as DjangoValidationError
from django.db.models import ProtectedError as DjangoProtectedError
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.views import exception_handler as drf_exception_handler

import re


def exception_handler(exc, context):
    """Handle Django ValidationError as an accepted exception"""

    if isinstance(exc, DjangoValidationError):
        exc = DRFValidationError(detail=exc.message_dict)

    if isinstance(exc, DjangoProtectedError):
        matches = re.search(r"\(\"([^()]+)\"", exc.args.__str__())
        exc = DRFValidationError(
            detail={
                "error": {
                    "type": str(exc.__class__.__name__),
                    "message": matches.group(1) if matches else _('It is not possible to delete this object.')
                },
                "protected_elements": [
                    {
                        "id": protected_object.pk,
                        "model": str(protected_object._meta.model.__name__),
                        "label": protected_object.__str__()
                    }
                    for protected_object in exc.protected_objects
                ]
            }
        )

    return drf_exception_handler(exc, context)
