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
        operation_description="City List",
        responses=response_schema,
    )
    def list(self, request):
        data = city_list()
        return ApiResponseDetailMixin(
            data=data,
            message="City list retrieve successfully",
            status_message="successful",
            status=status.HTTP_200_OK,
        )

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
