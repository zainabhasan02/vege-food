from django.shortcuts import render
from django.views import View

from cart.models import Cart

from blogs.models import Blog


# Create your views here.
class BlogView(View):
    def get(self, request):
        user_cart_items = Cart.objects.filter(user=request.user)
        cart_items_count = user_cart_items.count()  # Count the number of cart items

        blog_list = Blog.objects.filter(is_active=True).order_by('order')
        print("blog_list", blog_list)

        return render(request, 'blog.html', {'cart_items_count_k': cart_items_count, 'blog_list_k': blog_list})


class SingleBlogView(View):
    def get(self, request):
        user_cart_items = Cart.objects.filter(user=request.user)
        cart_items_count = user_cart_items.count()  # Count the number of cart items

        return render(request, 'single-blog.html', {'cart_items_count_k': cart_items_count})
