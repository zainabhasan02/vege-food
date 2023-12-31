from decimal import Decimal

from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=500, null=True, blank=True, verbose_name="category_name")
    active = models.BooleanField(default=True, null=True, blank=True, verbose_name="active")
    order = models.IntegerField(null=True, blank=True, verbose_name="order")
    addtime = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="addtime")
    category_image = models.ImageField(upload_to='category_images', null=True, blank=True,
                                       verbose_name="category_image")
    add_to_homepage = models.BooleanField(default=True, null=True, blank=True, verbose_name="add_to_homepage")

    def __str__(self):
        return self.category_name  # use for showing names

    class Meta:
        ordering = ["category_name"]


class Product(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True, verbose_name="name")
    description = models.TextField(null=True, blank=True, verbose_name="description")
    product_image = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name="product_image")
    out_of_stock = models.BooleanField(default=False, null=True, blank=True, verbose_name="out_of_stock")
    price = models.IntegerField(null=True, blank=True, verbose_name="price")
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="discount_percentage")
    product_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name="product_category")
    product_order = models.IntegerField(default=0, null=True, blank=True, verbose_name="product_order")
    add_to_home = models.BooleanField(default=False, null=True, blank=True, verbose_name="add_to_home")
    addtime = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="addtime")
    active = models.BooleanField(default=True, null=True, blank=True, verbose_name="active")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    def calculate_discounted_amount(self):
        if self.discount_percentage is not None:
            # calculated_discount = (self.price * self.discount_percentage) / 100
            # discounted_amount = self.price - calculated_discount

            calculated_discount = (Decimal(self.price) * Decimal(self.discount_percentage)) / Decimal(100)
            discounted_amount = Decimal(self.price) - calculated_discount

            return discounted_amount

        else:
            return None


class HomepageBanner(models.Model):
    banner_image = models.ImageField(upload_to='banner_images')
    banner_text = models.CharField(max_length=255, null=True, blank=True)
    banner_url = models.CharField(max_length=255, null=True, blank=True)
    button_text = models.CharField(max_length=100, null=True, blank=True)
    active_banner = models.BooleanField(default=True, null=True, blank=True)
    order_banner = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["banner_text"]


class DealOfDay(models.Model):
    deal_name = models.CharField(max_length=500)
    deal_image = models.ImageField(upload_to='deal_image')
    deal_url = models.CharField(max_length=255)
    active_deal = models.BooleanField()

    def __str__(self):
        return self.deal_name

    class Meta:
        ordering = ["deal_name"]
