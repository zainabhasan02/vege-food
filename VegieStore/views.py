from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from product.models import ProductCategory, Product, HomepageBanner, DealOfDay

from users.models import SatisfiedCustomer, SubscriberEmail


class IndexView(View):
    def get(self, request):
        product_category = ProductCategory.objects.filter(active=True).order_by('order')
        print("product_category..", product_category)

        product_list_data = Product.objects.filter(active=True).order_by('product_order')
        print("product_list_data..Index", product_list_data)

        homepage_banner_data = HomepageBanner.objects.filter(active_banner=True).order_by('order_banner')
        print("homepage_banner_data..", homepage_banner_data)

        deal_of_day_data = DealOfDay.objects.filter(active_deal=True).first()
        print("deal_of_day_data..", deal_of_day_data)

        satisfied_customer_data = SatisfiedCustomer.objects.filter(active_customer=True).order_by('customer_order')
        print("satisfied_customer_data..", satisfied_customer_data)

        # Retrieve the product instance from the database based on the product_id
        product_id = Product.objects.get(id=True)
        print("product_id..", product_id)

        # Call the calculate_discounted_amount method to get the discounted amount
        calculate_discounted_amount = product_id.calculate_discounted_amount()
        print("calculate_discounted_amount..", calculate_discounted_amount)

        return render(request, 'index.html',
                      {'homepage_banner_data_k': homepage_banner_data, 'product_category_k': product_category,
                       'product_list_data_k': product_list_data, 'deal_of_day_data_k': deal_of_day_data,
                       'satisfied_customer_data_k': satisfied_customer_data,
                       })

    def post(self, request):
        subscriber_email = request.POST.get('subscriber_email')
        existing_email = SubscriberEmail.objects.filter(email=subscriber_email)
        print("existing_email..", existing_email)
        if existing_email:
            print("Email already exists")
            pass
        else:
            SubscriberEmail.objects.create(email=subscriber_email)
            print("Created new email")
            print("New Subscriber Email Saved:", subscriber_email)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class AboutUsView(View):
    def get(self, request):
        return render(request, 'about.html')


class ContactUsView(View):
    def get(self, request):
        return render(request, 'contact.html')
