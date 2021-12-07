from .serializers import StadiumSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Stadium
from rest_framework import viewsets


class StadiumView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = StadiumSerializer
    http_method_names = ['get', 'post', 'put']
    queryset = Stadium.objects.all()