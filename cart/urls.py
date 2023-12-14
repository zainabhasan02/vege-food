from django.conf.urls import url

from cart.views import AddToCartView, CartView, CheckoutView, ShopView, WishlistView, AddToWishlistView
from django.urls import path

from cart import views

app_name = 'cart'
urlpatterns = [
    # Map the add_to_cart method to a URL with a product_id parameter
    path('add_to_cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    # Map the get method to a URL for viewing the cart
    path('view_cart/', CartView.as_view(), name='view_cart'),
    path('delete_cart_item/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),

    # Map the add_to_wishlist method to a URL with a product_id parameter
    path('add_to_wishlist/<int:product_id>/', AddToWishlistView.as_view(), name='add_to_wishlist'),
    # Map the get method to a URL for viewing the wishlist
    path('view_wishlist/', WishlistView.as_view(), name='view_wishlist'),
    path('delete_wishlist_item/<int:item_id>/', views.delete_wishlist_item, name='delete_wishlist_item'),

    url(r'^shop/$', ShopView.as_view(), name='shop'),
    path('shop/<str:category>/', ShopView.as_view(), name='shop_by_category'),

]
