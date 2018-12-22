from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from accounts.forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            # username = form.cleaned_data['username']
            # raw_password = form.cleaned_data['password1']
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})
