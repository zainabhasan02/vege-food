from django.conf.urls import url

from VegieStore.views import IndexView

from users.views import AboutUsView, ContactUsView

app_name = 'users'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='subscriber_email_form'),
    url(r'^about/$', AboutUsView.as_view(), name='about'),
    url(r'^contact/$', ContactUsView.as_view(), name='contact'),
    url(r'^contact_saved/$', ContactUsView.as_view(), name='contact_saved'),
]
