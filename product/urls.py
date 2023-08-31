from django.conf.urls import url

from product.views import SingleProductView, ProductCategoryDetailsListView, ProductListView

app_name = 'product'
urlpatterns = [
    # url(r'^$', SingleProductView.as_view(), name='single_product'),
    url(r'^single_product/(?P<single_product_id>\d+)$', SingleProductView.as_view(), name='single_product'),
    url(r'^product_category_details/(?P<product_category_details_id>\d+)$', ProductCategoryDetailsListView.as_view(),
        name='product_category_details'),
    url(r'^product_list/(?P<product_list_id>\d+)$', ProductListView.as_view(), name='product_list'),

]
