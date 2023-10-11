from django.contrib.auth.models import User
from django.db import models

from product.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    addtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f'Cart for {self.user.username}'
        return f'Cart for {self.user.username} - Product: {self.product}'

    class Meta:
        ordering = ["user"]

    def calculate_total_price(self):
        total_price = self.product.price
