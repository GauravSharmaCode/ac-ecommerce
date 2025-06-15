from rest_framework import generics, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to list all products or create a new one.
    Supports search and ordering.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category', 'tags']
    ordering_fields = ['price', 'created_at', 'updated_at']


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a product by ID.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductByCategoryAPIView(APIView):
    """
    API view to return products by a given category.
    """

    def get(self, request, category):
        products = Product.objects.filter(category__iexact=category)

        if not products.exists():
            return Response(
                {"detail": f"No products found in category '{category}'."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
