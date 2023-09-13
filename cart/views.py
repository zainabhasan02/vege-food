from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger

from product.models import Product, ProductCategory


# Create your views here.
class CartView(View):
    def get(self, request):
        return render(request, 'cart.html')


class CheckoutView(View):
    def get(self, request):
        return render(request, 'checkout.html')


class ShopView(View):
    def get(self, request):
        active_product_category_list = ProductCategory.objects.filter(active=True).order_by('order')
        print("active_product_category_list..Shop", active_product_category_list)

        shop_product_list = Product.objects.filter(active=True).order_by('product_order')
        print("shop_product_list..", shop_product_list)

        try:
            page_number = request.GET.get('page', 1)
            print("URL page number..", page_number)
        except PageNotAnInteger:
            page_number = 1
        p = Paginator(shop_product_list, 10)
        shop_paginated_product = p.page(page_number)

        context = {
            'shop_product_list_k': shop_product_list,
            'active_product_category_list_k': active_product_category_list,
            'shop_paginated_product_k': shop_paginated_product,
        }

        return render(request, 'shop.html', context)


class WishlistView(View):
    def get(self, request):
        return render(request, 'wishlist.html')
