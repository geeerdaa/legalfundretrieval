from .models import Persone, Contacts
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, EmailInput

class PersoneForm(ModelForm):
    class Meta:
        model = Persone
        fields = ['name', 'email', 'phone', 'company', 'date',  'story']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name',
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email address',
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone',
            }),
            "company": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Scam company name',
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last transaction date',
            }),
            "story": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
            }),
        }


class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'phone', 'story']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name',
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email address',
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone',
            }),
            "story": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
            }),
        }