from django.conf.urls import url

from VegieStore.views import IndexView

app_name = 'users'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='subscriber_email_form'),
]
