from django.shortcuts import render
from django.views import View

from .models import Product, ProductCategory


# Create your views here.

class ProductCategoryDetailsListView(View):
    def get(self, request, product_category_details_id):
        prod_cat_id = ProductCategory.objects.filter(id=product_category_details_id)
        print("product_category_Details_id..", prod_cat_id)
        product_category_list_data = ProductCategory.objects.filter(active=True).order_by('order')
        print("product_category_list_data..", product_category_list_data)
        return render(request, 'product_category_detail.html',
                      {'prod_cat_id_k': prod_cat_id,
                       'product_category_list_data_k': product_category_list_data})


class ProductListView(View):
    def get(self, request, product_list_id):
        # Product.objects.filter.first()
        product_list_data = Product.objects.filter(id=product_list_id, active=True).order_by('product_order')
        print("product_list_data..", product_list_data)
        print("product_list_id..", product_list_id)
        return render(request, 'product_list.html', {'product_list_data_k': product_list_data})


class SingleProductView(View):
    def get(self, request, single_product_id):
        # Retrieve the single product using its ID
        single_product_ID = Product.objects.filter(id=single_product_id).first()
        print("single_product_ID..", single_product_ID)

        # Now, retrieve all products with the same category as the single product
        related_products = Product.objects.filter(product_category=single_product_ID.product_category).exclude(
            id=single_product_id)
        print("related_products..", related_products)

        return render(request, 'single-product.html',
                      {'single_product_data_k': single_product_ID, 'related_products_k': related_products})
