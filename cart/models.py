from django.contrib.auth.models import User
from django.db import models

from product.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    addtime = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)  # to store the quantity of each product in the cart

    class Meta:
        ordering = ["user"]

    def __str__(self):
        # return f'Cart for {self.user.username}'
        return f'Cart for {self.user.username} - Product: {self.product}'
        # return f'Cart for {self.user.username}'

    def calculate_total_price(self):
        total_price = 0

        # Iterate over items in the cart
        for cart_item in self.cartitem_set.all():  # Assuming 'CartItem' is the related name for the cart items
            product = cart_item.product

            # Check if the product has a discount
            if product.discount_percentage:
                discounted_amount = product.calculate_discounted_amount()
                total_price += discounted_amount * cart_item.quantity
                print("discounted_total_price", total_price)
            else:
                total_price += product.price * cart_item.quantity
                print("_total_price", total_price)

        return total_price


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Assuming you have a Product model
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Wishlist for {self.user.username} - Product: {self.product}'

    class Meta:
        ordering = ["user"]
