from django.conf.urls import url

from cart.views import AddToCartView, CartView, CheckoutView, ShopView, WishlistView
from django.urls import path

from cart import views

app_name = 'cart'
urlpatterns = [
    # url(r'^$', CartView.as_view(), name='cart'),
    # Map the add_to_cart method to a URL with a product_id parameter
    # path('add_to_cart/<int:product_id>/', CartView.as_view(), name='add_to_cart'),
    # path('add_to_cart/<int:product_id>/', CartView.as_view(), name='add_to_cart'),
    # Map the get method to a URL for viewing the cart
    # path('view_cart/', CartView.as_view(), name='view_cart'),

    path('add_to_cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('view_cart/', CartView.as_view(), name='view_cart'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),

    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^shop/$', ShopView.as_view(), name='shop'),
    path('shop/<str:category>/', ShopView.as_view(), name='shop_by_category'),
    url(r'^wishlist/$', WishlistView.as_view(), name='wishlist'),
]
