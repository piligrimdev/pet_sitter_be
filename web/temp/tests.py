from rest_framework.test import APITestCase
from rest_framework import status


class HealthCheckAPITest(APITestCase):

    def test_health_check_request_returns_ok(self):
        url = '/temp/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
