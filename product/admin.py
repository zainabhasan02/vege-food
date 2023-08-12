from django.contrib import admin

from .models import ProductCategory, Product


# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "active", "order", "addtime", "add_to_homepage")
    search_fields = ("category_name",)


# for improving Admin UI
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","out_of_stock", "price","discount_percentage","product_category","add_to_home","addtime","active")
    search_fields = ("name",)
    list_filter = ("product_category__category_name",)


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
