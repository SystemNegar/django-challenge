from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from stadium.models import Stadium


class MatchTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="user", email="foo@gmail.com", password='123'
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.stadium = Stadium.objects.create(name="StadiumTest", capacity=100)

    def test_match_post(self):
        match_create_api = self.client.post(
            "/api/v1/match/", {"stadium": self.stadium.id, "event_date": "2021-12-20T15:49:08.017Z", "team1": "T1", "team2": "T2"}, format="json"
        )
        # Test against status code
        self.assertEqual(match_create_api.status_code, 201)
        # Test against payload keys and types
        self.assertDictEqual(
            match_create_api.data,
            {
                'stadium': 1,
                'event_date': '2021-12-20T15:49:08.017000Z',
                'team1': 'T1', 'team2': 'T2'
                }
        )
        match_create_api_fail = self.client.post(
            "/api/v1/match/",
            {"stadium": self.stadium.id, "event_date": "2021-12-20T15:49:08.017Z", "team1": "T1", "team2": "T2"},
            format="json"
        )
        # failed because of distinct datetime
        self.assertEqual(match_create_api_fail.status_code, 400)
