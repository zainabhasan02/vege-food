from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from users.models import SatisfiedCustomer, SubscriberEmail, ContactUs, BillingAddress

from cart.models import Cart


# Create your views here.


class AboutUsView(View):
    def get(self, request):
        satisfied_customer_data = SatisfiedCustomer.objects.filter(active_customer=True).order_by('customer_order')
        print("satisfied_customer_data--About..", satisfied_customer_data)

        user_cart_items = Cart.objects.filter(user=request.user)
        cart_items_count = user_cart_items.count()  # Count the number of cart items

        return render(request, 'about.html',
                      {'satisfied_customer_data_k': satisfied_customer_data, 'cart_items_count_k': cart_items_count})

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
        user_cart_items = Cart.objects.filter(user=request.user)
        cart_items_count = user_cart_items.count()  # Count the number of cart items

        return render(request, 'contact.html', {'cart_items_count_k': cart_items_count})

    def post(self, request):
        name = request.POST.get('names')
        email = request.POST.get('emails')
        subject = request.POST.get('subjects')
        message = request.POST.get('messages')

        new_user_created = ContactUs.objects.create(name=name, email=email, subject=subject, message=message)
        print("new_user_", new_user_created, "created..")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class CheckoutView(View):
    def get(self, request):
        user_cart_items = Cart.objects.filter(user=request.user)
        cart_items_count = user_cart_items.count()  # Count the number of cart items

        return render(request, 'checkout.html', {'cart_items_count_k': cart_items_count})

    def post(self, request):
        f_name = request.POST.get('firstname')
        l_name = request.POST.get('lastname')
        street1 = request.POST.get('street1')
        street2 = request.POST.get('street2')
        city = request.POST.get('town')
        postal = request.POST.get('zip')
        phone = request.POST.get('phn_num')
        email = request.POST.get('email')

        billing_address = BillingAddress.objects.create(first_name=f_name, last_name=l_name, street1=street1,
                                                        street2=street2,
                                                        city=city, post_code=postal, phone=phone, email=email)
        print("billing_address, ", billing_address)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
