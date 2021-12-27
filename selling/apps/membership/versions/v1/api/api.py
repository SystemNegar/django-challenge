from rest_framework.views import APIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView

from selling.apps.membership.versions.v1.services.user_services import UserService
from selling.tools.helper import Helper
from selling.tools.response import response_ok, response400


class RegisterAPIView(APIView):
    def post(self, request):
        try:
            body = Helper.get_dict_from_json(request.body)
            data = UserService.create_user(body)
        except Exception as e:
            return response400(
                request,
                error=e
            )
        return response_ok(
            request,
            data=data,
        )


class LoginAPIView(JSONWebTokenAPIView):
    serializer_class = JSONWebTokenSerializer

    def post(self, request, **kwargs):
        try:
            body = Helper.get_dict_from_json(request.body)
            login_data = UserService.login_user(body)
        except Exception as e:
            return response400(
                request,
                error=e,
            )

        super_response = super().post(
            request,
            **login_data,
        )
        if super_response.status_code == 200:
            data = {'token': super_response.data['token']}

            return response_ok(request, data=data)
        else:
            return response400(
                request,
                error="Invalid username or password",
            )
