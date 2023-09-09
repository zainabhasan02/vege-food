from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from users.models import Login, Signup, SatisfiedCustomer, SubscriberEmail, ContactUs


# Create your views here.
class LoginView(View):
    def get(self, request):

        return render(request, 'login.html')

    def post(self, request):
        login_email = request.POST.get('email')
        existing_email = Login.objects.filter(email=login_email)
        print("existing_email..", existing_email)
        if existing_email:
            print("Email already exists")
            HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            Login.objects.create(email=login_email)
            print("Created new email \nNew Login Email Saved:", login_email)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class SignupView(View):
    def get(self, request):

        return render(request, 'signup.html')

    def post(self, request):
        full_name = request.POST.get('full_name')
        signup_email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        existing_email = Signup.objects.filter(email=signup_email)
        print("existing_email..", existing_email)
        if existing_email:
            print("Email already exists")
            HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            Signup.objects.create(f_name=full_name, email=signup_email, password=password,
                                  confirm_password=confirm_password)
            print("New user successfully created:", full_name)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class AboutUsView(View):
    def get(self, request):
        satisfied_customer_data = SatisfiedCustomer.objects.filter(active_customer=True).order_by('customer_order')
        print("satisfied_customer_data--About..", satisfied_customer_data)

        return render(request, 'about.html', {'satisfied_customer_data_k': satisfied_customer_data})

    def post(self, request):
        subscriber_email = request.POST.get('subscriber_email')
        existing_email = SubscriberEmail.objects.filter(email=subscriber_email)
        print("existing_email..", existing_email)
        if existing_email:
            print("Email already exists")
            HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            SubscriberEmail.objects.create(email=subscriber_email)
            print("Created new email \nNew Subscriber Email Saved:", subscriber_email)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class ContactUsView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('names')
        email = request.POST.get('emails')
        subject = request.POST.get('subjects')
        message = request.POST.get('messages')

        new_user_created = ContactUs.objects.create(name=name, email=email, subject=subject, message=message)
        print("new_user_", new_user_created, "created..")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
