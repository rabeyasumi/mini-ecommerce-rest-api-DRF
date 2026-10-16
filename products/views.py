from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as django_filters

from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductSerializer

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte'
    )
    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte'
    )

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price']
        
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = ProductFilter
    filterset_fields = ['category']
    search_fields = ['name']
    ordering_fields = ['price', 'created_at']
    ordering = ['id']
    permission_classes = [AllowAny]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
