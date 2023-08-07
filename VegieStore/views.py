from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class AboutUsView(View):
    def get(self, request):
        return render(request, 'about.html')


class ContactUsView(View):
    def get(self, request):
        return render(request, 'contact.html')
