from django.shortcuts import render, redirect
from .forms import PersoneForm, ContactsForm


def index(request):
    data = {
        'title': 'Home',
    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'About Us',
    }
    return render(request, 'main/about-us/index.html', data)


def contacts(request):
    error = ''
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            error = 'Error'
    
    form = ContactsForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/about-us/contact-us/index.html', data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = PersoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            error = 'Error'

    form = PersoneForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/file-a-complaint/index.html', data)