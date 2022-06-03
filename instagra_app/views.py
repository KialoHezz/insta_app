from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def home(request):
    
    return render(request, 'home/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request, f'Hi {username}, Your Account was created sccessfully')

            return redirect('login')

    else:
        form = UserRegisterForm()

    ctx = {"form": form}

    return render(request, 'auth/register.html',ctx)

