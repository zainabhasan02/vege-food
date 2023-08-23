from django.contrib import admin

from users.models import SatisfiedCustomer, SubscriberEmail


# Register your models here.
class SatisfiedCustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "customer_order", "active_customer")
    search_fields = ("name",)


class SubscriberEmailAdmin(admin.ModelAdmin):
    list_display = ("email", "active_email", "created_at")
    search_fields = ("email",)


admin.site.register(SatisfiedCustomer, SatisfiedCustomerAdmin)
admin.site.register(SubscriberEmail, SubscriberEmailAdmin)
