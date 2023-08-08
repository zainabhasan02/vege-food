from django.conf.urls import url

from product.views import SingleProductView

urlpatterns = [
    url(r'^$', SingleProductView.as_view(), name='single_product'),
]
