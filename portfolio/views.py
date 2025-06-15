from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
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
            
