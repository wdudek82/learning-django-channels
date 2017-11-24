from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout


def user_list(request):
    return render(request, 'example/user_list.html')


def log_in(request):
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('example:user_list'))
        else:
            print(form.errors)
    return render(request, 'example/log_in.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect(reverse('example:log_in'))


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('example:log_in'))
        else:
            print(form.errors)
    return render(request, 'example/sign_up.html', {'form': form})
