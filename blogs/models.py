from django.db import models


# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True, verbose_name="name")
    description = models.TextField(null=True, blank=True, verbose_name="description")
    blog_image = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name="product_image")
    caption = models.BooleanField(default=False, null=True, blank=True, verbose_name="out_of_stock")
    price = models.IntegerField(null=True, blank=True, verbose_name="price")
    discount_percentage = models.IntegerField(null=True, blank=True, verbose_name="discount_percentage")
    product_order = models.IntegerField(default=0, null=True, blank=True, verbose_name="product_order")
    add_to_home = models.BooleanField(default=False, null=True, blank=True, verbose_name="add_to_home")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="addtime")
    active = models.BooleanField(default=True, null=True, blank=True, verbose_name="active")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
