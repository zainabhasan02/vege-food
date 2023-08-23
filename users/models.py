from django.db import models


# Create your models here.
class SatisfiedCustomer(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='satisfied_customer_images')
    active_customer = models.BooleanField(default=True)
    customer_order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class SubscriberEmail(models.Model):
    email = models.CharField(max_length=255)
    active_email = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']
