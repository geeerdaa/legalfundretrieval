from .models import User
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, NumberInput, EmailInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'company', 'date',  'story',]

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
