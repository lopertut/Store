from django.shortcuts import render, redirect
from . authorization import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')


def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('index')

    context = {
        'login_form': form
    }

    return render(request, 'login_form.html', context)


def logout(request):
    auth.logout(request)
    return redirect('index')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'registration_form': form
    }

    return render(request, 'registration_form.html', context=context)
