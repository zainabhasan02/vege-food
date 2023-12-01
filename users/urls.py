from django.conf.urls import url

from VegieStore.views import IndexView
from django.urls import path

from users.views import AboutUsView, ContactUsView, CheckoutView

app_name = 'users'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='subscriber_email_form'),
    url(r'^login/$', AboutUsView.as_view(), name='login'),
    url(r'^signup/$', AboutUsView.as_view(), name='signup'),
    url(r'^about/$', AboutUsView.as_view(), name='about'),
    url(r'^contact/$', ContactUsView.as_view(), name='contact'),
    url(r'^billing_address/$', CheckoutView.as_view(), name='billing_address'),
    # path('checkout/', CheckoutView.as_view(), name='checkout'),
]
