from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
import logging

from .models import Project
from .serializers import ProjectSerializer

logger = logging.getLogger(__name__)

class ProjectListAPIView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        """
        Return all Project objects. You can later filter by status, year, etc.
        """
        return Project.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception("Error fetching projects:")
            return Response(
                {"error": "Failed to fetch projects"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
