from django import forms
from .models import Subscriber, ContactMessage


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your firstname'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your lastname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email address'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your subject of this message'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Say something about us'}),
        }
