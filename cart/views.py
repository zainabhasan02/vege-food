from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

from product.models import Product, ProductCategory

from cart.models import Cart


# Create your views here.

class AddToCartView(View):
    def get(self, request, product_id):
        if request.user.is_authenticated:
            product = Product.objects.get(id=product_id)
            # Add product to cart logic goes here
            cart_item = Cart.objects.create(user=request.user, product=product)
            cart_item.save()
            user_cart_item = Cart.objects.filter(product__name=product)

            # quantity = request.POST.get('quantity', 1)  # Default to 1 if quantity is not provided
            # # Convert quantity to an integer if needed
            # try:
            #     quantity = int(quantity)
            # except ValueError:
            #     quantity = 1  # Default to 1 if quantity is not a valid integer
            #
            # # Perform your calculations with quantity and product.price
            # total_price = quantity * product.price
            # print("total_price..", total_price)

            print("product id for cart is ", product)
            print("cart_item", cart_item)

            return redirect('cart:view_cart')
        else:
            # Handle the case where the user is not authenticated
            return redirect('accounts:login')  # Redirect to the login page


class CartView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_cart_items = Cart.objects.filter(user=request.user)
            print("user_cart_item", user_cart_items)
            return render(request, 'cart.html', {'user_cart_items_k': user_cart_items})
        else:
            # Handle the case where the user is not authenticated
            return redirect('accounts:login')  # Redirect to the login page


def delete_item(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')

class CheckoutView(View):
    def get(self, request):
        return render(request, 'checkout.html')


class ShopView(View):
    def get(self, request, category=None):
        # Fetch all active product categories
        active_categories = ProductCategory.objects.filter(active=True).order_by('order')
        print("active_categories,Cart", active_categories)

        # Fetch all active products
        shop_product_list = Product.objects.filter(active=True).order_by('product_order')
        print("shop_product_list, Cart", shop_product_list)

        try:
            page_number = int(request.GET.get('page', 1))
            print("URL page number..", page_number)
        except (PageNotAnInteger, ValueError, TypeError):
            page_number = 1  # Default to 1 if an invalid value is provided

        # Filter products based on the selected category if category is specified
        if category:
            # shop_product_list = shop_product_list.filter(product_category=category)
            shop_product_list = shop_product_list.filter(product_category__category_name=category)
            print("Selected Category, Cart", shop_product_list)

        p = Paginator(shop_product_list, 2)
        print("p.....", p.num_pages)

        try:
            shop_paginated_product = p.page(page_number)
        except EmptyPage:
            # Handle when the requested page is out of range, for example, redirect to the last available page
            shop_paginated_product = p.page(p.num_pages)

        print("shop_paginated_product..", shop_paginated_product)

        context = {
            'selected_category_k': category,
            'shop_product_list_k': shop_product_list,
            'active_categories_k': active_categories,
            'shop_paginated_product_k': shop_paginated_product,
        }

        return render(request, 'shop.html', context)


class WishlistView(View):
    def get(self, request):
        return render(request, 'wishlist.html')
