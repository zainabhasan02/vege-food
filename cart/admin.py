from django.contrib import admin

from cart.models import Cart


# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "addtime")
    search_fields = ("user",)


admin.site.register(Cart, CartAdmin)
