from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from selling.apps.stadium.models import Stadium
from selling.apps.stadium.versions.v1.serializers.stadium_serializer import StadiumSerializer
from selling.tools.response import response_ok, response400


class StadiumAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = StadiumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response_ok(request, message="Stadium created successfully")

        return response400(request, error=serializer.errors)
