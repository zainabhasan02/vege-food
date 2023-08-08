from django.shortcuts import render
from django.views import View


# Create your views here.
class CartView(View):
    def get(self, request):
        return render(request, 'cart.html')


class CheckoutView(View):
    def get(self, request):
        return render(request, 'checkout.html')


class ShopView(View):
    def get(self, request):
        return render(request, 'shop.html')


class WishlistView(View):
    def get(self, request):
        return render(request, 'wishlist.html')
