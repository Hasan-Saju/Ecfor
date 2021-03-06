from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from Authentication.forms import CreateUserForm
# Create your views here.


@csrf_exempt
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('Communication:index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)  # render the form data
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(
                    request, 'Account is created successfully for ' + user)
                return redirect('Authentication:login')

        context = {'form': form}
        return render(request, 'register-2.html', context=context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Communication:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Communication:index')
            else:
                messages.info(request, "Username or Password is incorrect.")

        context = {}
        return render(request, 'login-2.html', context)


@login_required(login_url='Authentication:login')
def logoutUser(request):
    logout(request)
    return redirect('Authentication:login')
