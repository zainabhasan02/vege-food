from django.db.models import Count
from django.shortcuts import render
from django.views import View

from cart.models import Cart

from blogs.models import Blog

from product.models import ProductCategory, Product


# Create your views here.
class BlogView(View):
    def get(self, request):
        user_cart_items = Cart.objects.filter(user=request.user)
        cart_items_count = user_cart_items.count()  # Count the number of cart items

        blog_list = Blog.objects.filter(is_active=True).order_by('order')
        print("blog_list", blog_list)

        active_product_category = ProductCategory.objects.filter(active=True).order_by('order')
        print("active_product_category..", active_product_category)
        category_counts = []  # List to store category counts

        for category in active_product_category:
            active_product_count = Product.objects.filter(product_category=category, active=True).count()
            category_counts.append({'category': category, 'product_count': active_product_count})
            print("category_counts..", category_counts)

    # active_categories = ProductCategory.objects.filter(active=True)
    # categories_with_counts = active_categories.annotate(product_count=Count('product'))
    # print("active_categories", active_categories)
    # print("categories_with_counts", categories_with_counts)

        context = {
            'cart_items_count_k': cart_items_count, 'blog_list_k': blog_list,
            'categories_with_counts': category_counts
        }

        return render(request, 'blog.html', context)


class SingleBlogView(View):
    def get(self, request):
        user_cart_items = Cart.objects.filter(user=request.user)
        cart_items_count = user_cart_items.count()  # Count the number of cart items

        active_product_category = ProductCategory.objects.filter(active=True).order_by('order')
        print("active_product_category..", active_product_category)
        category_counts = []  # List to store category counts

        for category in active_product_category:
            category_count = Product.objects.filter(product_category=category, active=True).aggregate(
                total_products=Count('id'))
            category_counts.append({'category': category, 'total_products': category_count['total_products']})
            print("category_counts..", category_counts)

        return render(request, 'single-blog.html',
                      {'cart_items_count_k': cart_items_count, 'active_product_category_k': active_product_category,
                       'category_products_count_k': category_counts})
