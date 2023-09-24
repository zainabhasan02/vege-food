from django.conf.urls import url

from accounts.views import Register, Login, Logout

app_name = 'accounts'
urlpatterns = [
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    # url(r'^shop/$', ShopView.as_view(), name='shop'),

]
