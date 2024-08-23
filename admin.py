from django.contrib import admin
from .models import Subscriber, ContactMessage


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscription_date')
    search_fields = ('email',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'responded')
    list_filter = ('responded',)
    search_fields = ('first_name', 'last_name', 'email', 'subject')
