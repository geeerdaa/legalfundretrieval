from django.shortcuts import render, redirect
from .forms import UserForm



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
    data = {
        'title': 'Contacts Us',
    }
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            error = 'Error'

    form = UserForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/about-us/contact-us/index.html', data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            error = 'Error'

    form = UserForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/file-a-complaint/index.html', data)