from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from arman.api.mixins import ApiErrorsMixin, ApiResponseDetailMixin
from arman.api.schemas import response_schema

from .services import city_list


class CityApi(ApiErrorsMixin, ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="City list",
        responses=response_schema,
    )
    def list(self, request):

        data = city_list()

        return ApiResponseDetailMixin(
            data=data,
            message="City list",
            status_message="successful",
            status=status.HTTP_200_OK,
        )
