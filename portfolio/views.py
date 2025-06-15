from django.conf import settings
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
import logging

from .models import Portfolio
from .serializers import PortfolioSerializer

logger = logging.getLogger(__name__)

class PortfolioListView(ListAPIView):
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        """
        Return only active Portfolio entries.
        """
        return Portfolio.objects.filter(is_active=True)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

            for item in data:
                logo_path = item.get("logo", "")
                if logo_path:
                    # Normalize logo path
                    if logo_path.startswith("/media/"):
                        full_url = request.build_absolute_uri(logo_path)
                    else:
                        full_url = request.build_absolute_uri(
                            f"/media/clients_logos/{logo_path.split('/')[-1]}"
                        )
                    item["logo"] = full_url

            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            logger.exception("Error fetching portfolio list:")
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
