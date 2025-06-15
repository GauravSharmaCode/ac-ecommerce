from django.shortcuts import render
from django.conf import settings
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

# Create your views here.
from .models import Portfolio
from .serializers import PortfolioSerializer

class PortfolioListView(ListAPIView):
    serializer_class = PortfolioSerializer

    def get_queryset(self):
             """
    Return a queryset of active Portfolio objects.

    This method filters the Portfolio objects to include only those
    that are marked as active.

    Returns:
        QuerySet: A QuerySet containing active Portfolio objects.
    """
            ###############################################################################
            # This method is used to filter the Portfolio objects to include only those
            # that are marked as active.
            ###############################################################################
             return Portfolio.objects.filter(is_active=True)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        # Patch logo field to include correct relative path
        for item in serializer.data:
            if item.get('logo'):
                # If logo path already starts with MEDIA_URL, use as is
                if item['logo'].startswith('/media/'):
                    item['logo'] = request.build_absolute_uri(item['logo'])
                else:
                    item['logo'] = request.build_absolute_uri('/media/clients_logos/' + item['logo'].split('/')[-1])
        return Response(serializer.data)

