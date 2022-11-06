from cgitb import reset
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from booking.models import Stadium, StadiumPlace, PlaceSeats, Match, Team, Ticket, Invoice
from booking.serializers import StadiumSerializer, StadiumPlaceSerializer,\
     PlaceSeatsSerializer, TeamSerializer, MatchSerializer, TicketSerializer, InvoiceSerilizer,\
        RetrieveInvoiceSerilizer, BuyInvoiceSerilizer


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


class TicketListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]


class TicketRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]


class CreateInvoiceAPI(generics.CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerilizer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)


class RetrieveUpdateInvoiceAPI(generics.RetrieveUpdateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerilizer
    permission_classes = [IsAuthenticated]
    serializer_classes = {
        'GET': RetrieveInvoiceSerilizer,
        'PUT': InvoiceSerilizer
    }
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_classes.get(self.request.method)
        return self.serializer_classes.get(self.request.method)


class BuyInvoiceAPI(generics.UpdateAPIView):
    """
    
    """
    queryset = Invoice.objects.all()
    serializer_class = BuyInvoiceSerilizer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
