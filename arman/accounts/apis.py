from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from arman.api.mixins import ApiErrorsMixin, ApiResponseDetailMixin
from arman.api.schemas import response_schema

from .serializers import LoginInputSerializer, OTPInputSerializer, SignupInputSerializer
from .services import login, register


class SignUpApi(ApiErrorsMixin, APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=SignupInputSerializer,
        security=[],
        operation_description="SignUp",
        responses=response_schema,
    )
    def post(self, request):
        serializer = SignupInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        register(phone=str(serializer.validated_data["phone"]))

        return ApiResponseDetailMixin(
            message="Account registered successfully",
            status=status.HTTP_200_OK,
            data=None,
            status_message="successful",
        )


class OTPApi(ApiErrorsMixin, APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=OTPInputSerializer,
        security=[],
        operation_description="OTP",
        responses=response_schema,
    )
    def post(self, request):
        serializer = OTPInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        register(phone=str(serializer.validated_data["phone"]))

        return ApiResponseDetailMixin(
            message="OTP registered successfully",
            status=status.HTTP_200_OK,
            data=None,
            status_message="successful",
        )


class LoginApi(ApiErrorsMixin, APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=LoginInputSerializer,
        security=[],
        operation_description="Login",
        responses=response_schema,
    )
    def post(self, request):
        serializer = LoginInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = login(
            otp=serializer.validated_data["otp"],
            phone=str(serializer.validated_data["phone"]),
        )

        return ApiResponseDetailMixin(
            message="User login successfully",
            status=status.HTTP_200_OK,
            data=data,
            status_message="successful",
        )
