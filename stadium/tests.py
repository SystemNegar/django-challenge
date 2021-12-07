from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class StadiumTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="user", email="foo@gmail.com", password='123'
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_stadium_post(self):
        stadium_create_api = self.client.post(
            "/api/v1/stadium/", {"name": "stadium3", "capacity": 100}, format="json"
        )
        # Test against status code
        self.assertEqual(stadium_create_api.status_code, 201)
        # Test against payload keys and types
        self.assertDictEqual(
            stadium_create_api.data,
            {'id': 1, 'name': 'stadium3', 'founded_in': stadium_create_api.data.get("founded_in"), 'capacity': 100}
        )
