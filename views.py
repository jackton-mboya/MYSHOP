from django.shortcuts import render, redirect
from django.conf import settings
from rest_framework import generics
from .models import Subscriber, ContactMessage
from .forms import SubscriptionForm, ContactForm
from .serializers import SubscriberSerializer, ContactMessageSerializer
from django.core.mail import send_mail
from .paypal_config import paypalrestsdk


# PayPal payment creation view
def create_payment(request):
    paypalrestsdk.configure({
        "mode": settings.PAYPAL_MODE,
        "client_id": settings.PAYPAL_CLIENT_ID,
        "client_secret": settings.PAYPAL_CLIENT_SECRET
    })

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": request.build_absolute_uri('/paypal/execute/'),
            "cancel_url": request.build_absolute_uri('/paypal/cancel/')
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "Item Name",
                    "sku": "item",
                    "price": "10.00",
                    "currency": "USD",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": "10.00",
                "currency": "USD"
            },
            "description": "Payment for items."
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = link.href
                return redirect(approval_url)
    else:
        return render(request, 'error.html', {'error': payment.error})


# PayPal payment execution view
def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return render(request, 'success.html', {'payment': payment})
    else:
        return render(request, 'error.html', {'error': payment.error})


# PayPal payment cancellation view
def payment_cancelled(request):
    return render(request, 'cancel.html')


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            Subscriber.objects.create(email=email)
            send_mail(
                'Subscription Confirmation',
                'Thank you for subscribing!',
                'jacktonmboya1@gmail.com',
                [email],
                fail_silently=False,
            )
            return redirect('subscription_success')  # Redirect to a thank-you page
    else:
        form = SubscriptionForm()
    return render(request, 'subscribe.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    contact_info = {
        'contact_address': '423 Utawala, Nairobi, Kenya',
        'contact_phone': '+254799877727',
        'contact_email': 'jacktonmboya1@gmail.com',
        'contact_url': 'http://jacktonmboya.com'
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Contact Message Received',
                'Thank you for reaching out! We will get back to you soon.',
                'jacktonmboya1@gmail.com',
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('contact_success')
    else:
        form = ContactForm()

    context = {
        'form': form,
        **contact_info
    }

    return render(request, 'contact.html', context)


def product(request):
    return render(request, 'product.html')


def services(request):
    return render(request, 'services.html')


def single(request):
    return render(request, 'single.html')


def help_view(request):
    return render(request, 'help.html')


def terms(request):
    return render(request, 'terms.html')


def meetups(request):
    return render(request, 'meetups.html')


def help_desk(request):
    return render(request, 'help_desk.html')


def shop(request):
    return render(request, 'shop.html')


def privacy(request):
    return render(request, 'privacy.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def handbook(request):
    return render(request, 'handbook.html')


def find_developers(request):
    return render(request, 'find_developers.html')


def find_designers(request):
    return render(request, 'find_designers.html')


def teams(request):
    return render(request, 'teams.html')


def advertise(request):
    return render(request, 'advertise.html')


def API(request):
    return render(request, 'API.html')


def cart_view(request):
    return render(request, 'cart.html')


def contact_success(request):
    return render(request, 'contact_success.html')


def web_design(request):
    return render(request, 'web_design.html')


def ecommerce(request):
    return render(request, 'ecommerce.html')


def branding(request):
    return render(request, 'branding.html')


def payment_view(request):
    return render(request, 'payment.html')


def subscription_success(request):
    return render(request, 'subscription_success.html')


def process_payment_view(request):
    if request.method == 'POST':
        return redirect('payment')
    return render(request, 'payment.html')


# API views
class SubscriberListCreateView(generics.ListCreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class SubscriberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class ContactMessageListCreateView(generics.ListCreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer


class ContactMessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
