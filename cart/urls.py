from django.conf.urls import url

from cart.views import CartView, CheckoutView, ShopView, WishlistView

urlpatterns = [
    url(r'^$', CartView.as_view(), name='cart'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^shop/$', ShopView.as_view(), name='shop'),
    url(r'^wishlist/$', WishlistView.as_view(), name='wishlist'),
]
