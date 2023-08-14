from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from product.models import ProductCategory


class IndexView(View):
    def get(self, request):
        product_category = ProductCategory.objects.filter(active=True).order_by('order')
        print("product_category..", product_category)
        return render(request, 'index.html', {'product_category_k': product_category})


class AboutUsView(View):
    def get(self, request):
        return render(request, 'about.html')


class ContactUsView(View):
    def get(self, request):
        return render(request, 'contact.html')
