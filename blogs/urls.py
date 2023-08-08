from django.conf.urls import url

from blogs.views import BlogView, SingleBlogView

urlpatterns = [
    url(r'^$', BlogView.as_view(), name='blog'),
    url(r'^single_blog/$', SingleBlogView.as_view(), name='single_blog'),
]
