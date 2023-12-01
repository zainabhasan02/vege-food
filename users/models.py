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


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class BillingAddress(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    street1 = models.CharField(max_length=255, null=True, blank=True)
    street2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True, blank=True)
    post_code = models.IntegerField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

# class Login(models.Model):
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.email
#
#     class Meta:
#         ordering = ['email']
#
#
# class Signup(models.Model):
#     f_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     confirm_password = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.f_name
#
#     class Meta:
#         ordering = ['f_name']
