from django.contrib import admin

from cart.models import Cart, CartItem, WishlistItem


# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "addtime")
    search_fields = ("user",)


class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "added_at")
    search_fields = ("user",)


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
admin.site.register(WishlistItem, WishlistItemAdmin)
