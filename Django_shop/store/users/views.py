from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth

# Create your views here.
def login(requset):
    if requset.method == 'POST':
        form = UserLoginForm(data=requset.POST)
        if form.is_valid():
            username = requset.POST['username']
            password = requset.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(requset, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(requset, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)
