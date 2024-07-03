from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Customer


def home(request):
    customers = Customer.objects.all()

    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect ('home')
        else:
            messages.success(request, 'There was an error logging in, please try again!')
            return redirect('home')
    else:
        return render(request, 'home.html', {'customers':customers})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been log out!')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully Register')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})
