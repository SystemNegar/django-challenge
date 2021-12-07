from .serializers import MatchSerializer
from .models import Match
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class MatchView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = MatchSerializer
    http_method_names = ['get', 'post', 'put']
    queryset = Match.objects.all()
