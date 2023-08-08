from django.shortcuts import render
from django.views import View


# Create your views here.
class BlogView(View):
    def get(self, request):
        return render(request, 'blog.html')


class SingleBlogView(View):
    def get(self, request):
        return render(request, 'single-blog.html')
