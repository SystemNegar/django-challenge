from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from stadium.models import Stadium
from matches.models import Match


class SeatTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="user", email="foo@gmail.com", password='123'
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.stadium = Stadium.objects.create(name="StadiumTest", capacity=100)
        self.match = Match.objects.create(stadium=self.stadium, event_date="2021-12-22T15:49:08.017Z", team1="FOO1", team2="FOO2")

    def test_seat_post(self):
        seat_create_api = self.client.post(
            "/api/v1/seat/", {"match": self.match.id, "row": 1, "column": 1, "seat_num": 1}, format="json"
        )
        # Test against status code
        self.assertEqual(seat_create_api.status_code, 201)
        # Test against payload keys and types
        self.assertDictEqual(
            seat_create_api.data,
            {'match': 1, 'row': 1, 'column': 1, 'seat_num': 1}
        )
