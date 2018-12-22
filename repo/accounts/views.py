from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})
