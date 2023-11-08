from django.contrib import admin

from users.models import SatisfiedCustomer, SubscriberEmail, ContactUs, BillingAddress


# Register your models here.


class SatisfiedCustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "customer_order", "active_customer")
    search_fields = ("name",)


class SubscriberEmailAdmin(admin.ModelAdmin):
    list_display = ("email", "active_email", "created_at")
    search_fields = ("email",)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "message")
    search_fields = ("name",)


class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ("first_name", "email", "city", "post_code", "phone")
    search_fields = ("first_name",)


# admin.site.register(Login, LoginAdmin)
# admin.site.register(Signup, SignupAdmin)
admin.site.register(SatisfiedCustomer, SatisfiedCustomerAdmin)
admin.site.register(SubscriberEmail, SubscriberEmailAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(BillingAddress, BillingAddressAdmin)
