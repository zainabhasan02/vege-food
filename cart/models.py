from django.contrib.auth.models import User
from django.db import models

from product.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    addtime = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)  # to store the quantity of each product in the cart

    def __str__(self):
        # return f'Cart for {self.user.username}'
        return f'Cart for {self.user.username} - Product: {self.product}'

    class Meta:
        ordering = ["user"]

    def calculate_total_cost(self):
        # Assuming you have an instance of the Cart model
        product = self.product
        quantity = self.quantity

        discounted_amount = product.calculate_discounted_amount()
        if discounted_amount is not None:
            total_cost = discounted_amount * quantity
        else:
            total_cost = product.price * quantity

        return total_cost


class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Assuming you have a Product model
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Wishlist for {self.user.username} - Product: {self.product}'

    class Meta:
        ordering = ["user"]

