from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from product.models import ProductCategory, Product, HomepageBanner


class IndexView(View):
    def get(self, request):
        product_category = ProductCategory.objects.filter(active=True).order_by('order')
        print("product_category..", product_category)

        product_list_data = Product.objects.filter(active=True).order_by('product_order')
        print("product_list_data..Index", product_list_data)

        homepage_banner_data = HomepageBanner.objects.filter(active_banner=True).order_by('order_banner')
        print("homepage_banner_data..", homepage_banner_data)

        return render(request, 'index.html',
                      {'homepage_banner_data_k': homepage_banner_data, 'product_category_k': product_category,
                       'product_list_data_k': product_list_data})


class AboutUsView(View):
    def get(self, request):
        return render(request, 'about.html')


class ContactUsView(View):
    def get(self, request):
        return render(request, 'contact.html')
