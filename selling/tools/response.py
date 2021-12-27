from collections import OrderedDict
from datetime import datetime

from rest_framework.response import Response


class RichResponse(Response):
    def __init__(
            self,
            request,
            data=None,
            status=200,
            error=None,
            hint=None,
            message=None,
            **kwargs
    ):
        resp = OrderedDict()

        # Check Type of 'error'.
        if isinstance(error, Exception):
            error = error.__str__()

        resp.update([
            ("status", status),
            ("error", error),
            ("hint", hint),
            ("message", message),
            ("time", datetime.now().timestamp()),
            ("data", data),
        ])

        for kw, val in kwargs.items():
            resp.update([
                (kw, val),
            ])

        super(RichResponse, self).__init__(data=resp, status=status)


def response_ok(req, data=None, message=None):
    return RichResponse(req, data=data, message=message, status=200)


def response4xx(req, data=None, status=None, error=None):
    if status is None:
        status = 400
    return RichResponse(req, data=data, status=status, error=error)


def response400(req, data=None, error=None):
    return RichResponse(req, data=data, status=400, error=error)


def response404(req, data=None, error=None):
    return RichResponse(req, data=data, status=404, error=error)


def response403(req, data=None, error=None):
    return RichResponse(req, data=data, status=403, error=error)


def response500(req, data=None, error=None):
    return RichResponse(req, data=data, status=500, error=error)


def response(
        request,
        status=200,
        data=None,
        error=None,
        hint=None,
        message=None,
        redirect_to=None,
        pagination=True,
        **kwargs
):
    return RichResponse(
        request=request,
        status=status,
        data=data,
        error=error,
        hint=hint,
        message=message,
        redirect_to=redirect_to,
        pagination=pagination,
        **kwargs,
    )