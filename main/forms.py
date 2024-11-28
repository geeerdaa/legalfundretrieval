from .models import Persone, Contacts
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, EmailInput, NumberInput

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
                'type': 'tel',
                'class': 'form-control',
                'pattern': '[+0-9]*',  # Разрешить только цифры
                'inputmode': 'numeric',  # Показывать числовую клавиатуру на мобильных устройствах
                'placeholder': 'Your Phone',
            }),
            "company": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Scam company name',
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'pattern': '[.0-9]*',  # Разрешить только цифры
                'inputmode': 'numeric',  # Показывать числовую клавиатуру на мобильных устройствах
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
                'type': 'tel',
                'class': 'form-control',
                'pattern': '[+0-9]*',  # Разрешить только цифры
                'inputmode': 'numeric',  # Показывать числовую клавиатуру на мобильных устройствах
                'placeholder': 'Your Phone',
            }),
            "story": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
            }),
        }