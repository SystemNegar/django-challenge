from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from booking.models import Stadium, StadiumPlace, PlaceSeats, Match, Team
from booking.serializers import StadiumSerializer, StadiumPlaceSerializer,\
     PlaceSeatsSerializer, TeamSerializer, MatchSerializer

class StadiumListCreateAPI(generics.ListCreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer 
    permission_classes = [IsAuthenticated]


class StadiumRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [IsAuthenticated]


class StadiumPlaceListCreateAPI(generics.ListCreateAPIView):
    queryset = StadiumPlace.objects.all()
    serializer_class = StadiumPlaceSerializer 


class StadiumPlaceRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = StadiumPlace.objects.all()
    serializer_class = StadiumPlaceSerializer
    permission_classes = [IsAuthenticated]


class PlaceSeatsListCreateAPI(generics.ListCreateAPIView):
    queryset = PlaceSeats.objects.all()
    serializer_class = PlaceSeatsSerializer 
    permission_classes = [IsAuthenticated]


class PlaceSeatsRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlaceSeats.objects.all()
    serializer_class = PlaceSeatsSerializer
    permission_classes = [IsAuthenticated]


class TeamListCreateAPI(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]


class TeamRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]


class MatchListCreateAPI(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer 
    permission_classes = [IsAuthenticated]


class MatchRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]


