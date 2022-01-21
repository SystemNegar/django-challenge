from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from arman.api.mixins import ApiErrorsMixin, ApiResponseDetailMixin
from arman.api.schemas import response_schema

from .serializers import UserSignupInputSerializer
from .services import user_signup


class UserSignupApi(ApiErrorsMixin, APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=UserSignupInputSerializer,
        security=[],
        operation_description="User SignUp",
        responses=response_schema,
    )
    def post(self, request):
        serializer = UserSignupInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = user_signup(phone=str(serializer.validated_data["phone"]))

        return ApiResponseDetailMixin(
            message="Account registered successfully",
            status=status.HTTP_200_OK,
            data={"token": token},
            status_message="successful",
        )
