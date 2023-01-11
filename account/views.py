from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('account:login')
        return HttpResponse('Invalid form')

    form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'account/register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:index')
            return HttpResponse('Not found this user')
        return HttpResponse('Invalid form')

    form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'account/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('account:login')
