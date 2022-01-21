from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from arman.api.mixins import ApiErrorsMixin, ApiResponseDetailMixin
from arman.api.schemas import response_schema

from .serializers import StadiumCreateInputSerializer
from .services import create_stadium


class StadiumApi(ApiErrorsMixin, ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=StadiumCreateInputSerializer,
        operation_description="Create Stadium",
        responses=response_schema,
    )
    def create(self, request):
        serializer = StadiumCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_stadium(**serializer.validated_data)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
