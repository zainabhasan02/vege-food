from django.conf.urls import url

from cart.views import CartView, CheckoutView, ShopView, WishlistView
from django.urls import path

app_name = 'cart'
urlpatterns = [
    url(r'^$', CartView.as_view(), name='cart'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^shop/$', ShopView.as_view(), name='shop'),
    # url(r'^shop/(?P<category>[\w-]+)/$', ShopView.as_view(), name='shop_by_category'),
    # url(r'^category_list/(?P<category_list_id>\d+)$', ShopView.as_view(), name='category_list'),
    path('shop/<str:category>/', ShopView.as_view(), name='shop_by_category'),
    url(r'^wishlist/$', WishlistView.as_view(), name='wishlist'),
]
