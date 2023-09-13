from django.contrib import admin

from .models import ProductCategory, Product, HomepageBanner, DealOfDay


# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "active", "order", "addtime", "add_to_homepage")
    search_fields = ("category_name",)


# for improving Admin UI
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name", "product_order", "add_to_home", "price", "discount_percentage", "active", "out_of_stock",
        "product_category", "addtime")
    search_fields = ("name",)
    list_filter = ("product_category__category_name",)


class HomepageBannerAdmin(admin.ModelAdmin):
    list_display = ("banner_text", "banner_url", "active_banner", "order_banner")
    search_fields = ("banner_text",)


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(HomepageBanner, HomepageBannerAdmin)
admin.site.register(DealOfDay)
