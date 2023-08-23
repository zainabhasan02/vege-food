from django.contrib import admin

from users.models import SatisfiedCustomer


# Register your models here.
class SatisfiedCustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "customer_order", "active_customer")
    search_fields = ("name",)


admin.site.register(SatisfiedCustomer, SatisfiedCustomerAdmin)
