from django.urls import path, include
from booking.views import StadiumListCreateAPI, StadiumRetrieveUpdateDestroyAPI, StadiumPlaceListCreateAPI,\
     StadiumPlaceRetrieveUpdateDestroyAPI, PlaceSeatsListCreateAPI, PlaceSeatsRetrieveUpdateDestroyAPI,\
     TeamListCreateAPI, TeamRetrieveUpdateDestroyAPI, MatchListCreateAPI, MatchRetrieveUpdateDestroyAPI,\
        TicketListCreateAPIView, TicketRetrieveUpdateDestroyAPI, CreateInvoiceAPI, RetrieveUpdateInvoiceAPI,\
            BuyInvoiceAPI

urlpatterns = [
    path('stadium', StadiumListCreateAPI.as_view()),
    path('stadium/<int:pk>', StadiumRetrieveUpdateDestroyAPI.as_view(), name='stadium_detail'),
    path('stadium-place', StadiumPlaceListCreateAPI.as_view()),
    path('stadium-place/<int:pk>', StadiumPlaceRetrieveUpdateDestroyAPI.as_view(), name='stadium_place_detail'),
    path('place-seats', PlaceSeatsListCreateAPI.as_view()),
    path('place-seats/<int:pk>', PlaceSeatsRetrieveUpdateDestroyAPI.as_view(), name='place_seats_detail'),
    path('team', TeamListCreateAPI.as_view()),
    path('team/<int:pk>', TeamRetrieveUpdateDestroyAPI.as_view(), name='team_detail'),
    path('match', MatchListCreateAPI.as_view()),
    path('match/<int:pk>', MatchRetrieveUpdateDestroyAPI.as_view(), name='match_detail'),
    path('ticket', TicketListCreateAPIView.as_view()),
    path('ticket/<int:pk>', TicketRetrieveUpdateDestroyAPI.as_view(), name='ticket_detail'),
    path('invoice', CreateInvoiceAPI.as_view()),
    path('invoice/<int:pk>', RetrieveUpdateInvoiceAPI.as_view()),
    path('invoice/<int:pk>/buy', BuyInvoiceAPI.as_view()),
]
