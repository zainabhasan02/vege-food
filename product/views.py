from django.shortcuts import render
from django.views import View


# Create your views here.
class SingleProductView(View):
    def get(self, request):
        return render(request, 'single-product.html')
