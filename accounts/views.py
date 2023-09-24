from django.contrib import messages
from django.forms import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User, auth


# Create your views here.
class Register(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        print("firstname..", firstname)
        print("lastname..", lastname)
        print("username..", username)
        print("email..", email)
        print("password..", password)
        print("confirm_password..", confirm_password)

        if password == confirm_password:
            # Check if a user with the same username already exists
            if User.objects.filter(username=username).exists():
                print(username, "Already exists user")
                messages.info(request, 'This username is already in use. Please choose another.')

            elif User.objects.filter(email=email).exists():
                print(username, "Email already taken")
                messages.info(request, 'Email already taken')

            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,
                                                email=email, password=password)
                user.save()
                print("new user created..", user)
                return redirect('accounts:login')
        else:
            messages.info(request, 'Password not matching')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        firstname = request.POST.get('first_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("username for login is", username)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('accounts:login')


class Logout(View):
    def get(self, request):
        auth.logout(request)
        return redirect("/")
