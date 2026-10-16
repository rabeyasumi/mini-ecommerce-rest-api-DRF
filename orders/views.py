from decimal import Decimal

from django.db import transaction
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Order
from .serializers import OrderSerializer
from products.models import Product


class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user
        ).select_related('product', 'user')

    @transaction.atomic
    def perform_create(self, serializer):
        product_id = self.request.data.get('product')
        quantity = self.request.data.get('quantity')

        try:
            quantity = int(quantity)
        except (TypeError, ValueError):
            raise ValidationError({
                'quantity': 'Enter a valid whole number.'
            })

        if quantity <= 0:
            raise ValidationError({
                'quantity': 'Quantity must be greater than zero.'
            })

        try:
            product = Product.objects.select_for_update().get(
                pk=product_id
            )
        except (Product.DoesNotExist, ValueError, TypeError):
            raise ValidationError({
                'product': 'Invalid product ID.'
            })

        if product.stock < quantity:
            raise ValidationError({
                'quantity': 'Not enough stock available.'
            })

        total_price = product.price * quantity

        product.stock -= quantity
        product.save(update_fields=['stock'])

        serializer.save(
            user=self.request.user,
            product=product,
            quantity=quantity,
            total_price=total_price,
        )


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user
        ).select_related('product', 'user')