import null as null
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
    discount_percentage = models.IntegerField(null=True, blank=True, verbose_name="discount_percentage")
    product_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name="product_category")
    product_order = models.IntegerField(default=0,null=True, blank=True, verbose_name="product_order")
    add_to_home = models.BooleanField(default=False, null=True, blank=True, verbose_name="add_to_home")
    addtime = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="addtime")
    active = models.BooleanField(default=True, null=True, blank=True, verbose_name="active")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
