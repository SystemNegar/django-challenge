from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from selling.apps.match.versions.v1.serializers.match_serializer import MatchSerializer
from selling.tools.response import response_ok, response400


class MatchAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response_ok(request, message="Match Created successfully")

        return response400(request, error=serializer.errors)
