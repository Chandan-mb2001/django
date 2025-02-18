# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']  # The user object from the form
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the home page after login
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
