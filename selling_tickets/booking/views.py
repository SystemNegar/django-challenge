from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from booking.models import Stadium, StadiumPlace, PlaceSeats
from booking.serializers import StadiumSerializer, StadiumPlaceSerializer,\
     PlaceSeatsSerializer


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
