from django.conf.urls import url

from VegieStore.views import IndexView

app_name = 'users'
urlpatterns = [
    url(r'^subscriber_email_form/$', IndexView.as_view(), name='subscriber_email_form'),
]
