"""
Views for test endpoint.
"""

from django.http import HttpRequest
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import add
from kombu.exceptions import OperationalError


class HealthCheckEndpoint(GenericAPIView):
    """
    Endpoint for app health check.
    """

    def get(self, request: HttpRequest) -> Response:
        """
        Returns result of celery delayed task.

        If django server can get a request and connect to
        RabbitMQ via celery, app is healthy.
        """
        try:
            trask_result = add.delay(2, 3)
            result = {'message': f'Task result of adding 2 and 3 is {trask_result}'}
        except OperationalError as e:
            result = {'message': "Can't connect to celery or RabbitMQ. Check logs for info"}
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(result)
