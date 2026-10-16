from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
