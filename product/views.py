from django.shortcuts import render
from django.views import View

from product.models import Product

from product.models import ProductCategory


# Create your views here.
class SingleProductView(View):
    def get(self, request):
        return render(request, 'single-product.html')


class ProductCategoryDetailsListView(View):
    def get(self, request, product_category_details_id):
        prod_cat_id = ProductCategory.objects.filter(id=product_category_details_id)
        print("product_category_Details_id..", prod_cat_id)
        product_list_data = Product.objects.filter(active=True).order_by('product_order')
        print("product_list_data..", product_list_data)

        return render(request, 'product_category_detail.html', {'prod_cat_id_k': prod_cat_id,
                                                                'product_list_data_k': product_list_data})


class ProductListView(View):
    def get(self, request, product_list_id):
        # filter.first
        product_list_data = Product.objects.filter(id=product_list_id, active=True).order_by('product_order')
        print("product_list_data..", product_list_data)
        print("product_list_id..", product_list_id)
        return render(request, 'product_list.html', {'product_list_data_k': product_list_data})
