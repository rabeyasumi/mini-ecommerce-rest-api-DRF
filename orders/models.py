from django.conf import settings
from django.db import models
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='orders'
    )
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user}"