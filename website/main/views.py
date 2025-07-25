from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request,'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request,'registration/sign_up.html',{'form':form})
