from django.contrib import admin

from users.models import Login, Signup, SatisfiedCustomer, SubscriberEmail, ContactUs


# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display = "email"
    search_fields = ("email",)


class SignupAdmin(admin.ModelAdmin):
    list_display = ("f_name", "email", "customer_order", "active_customer")
    search_fields = ("f_name",)


class SatisfiedCustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "customer_order", "active_customer")
    search_fields = ("name",)


class SubscriberEmailAdmin(admin.ModelAdmin):
    list_display = ("email", "active_email", "created_at")
    search_fields = ("email",)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "message")
    search_fields = ("name",)


# admin.site.register(Login, LoginAdmin)
# admin.site.register(Signup, SignupAdmin)
admin.site.register(SatisfiedCustomer, SatisfiedCustomerAdmin)
admin.site.register(SubscriberEmail, SubscriberEmailAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
