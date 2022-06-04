from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.dispatch import receiver

from .forms import UserRegisterForm,UserUpdateProfileForm,UpdateProfileForm
from .models import UserProfile
from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver


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


# @receiver(post_save, sender=User) 
@login_required
def profile(request,**kwargs):
    if request.method == 'POST':
        u_form = UserUpdateProfileForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST,request.FILES, instance=request.user)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

    

            messages.success(request,f"Your profile has been updated")

            return redirect('profile')

    else:
        u_form = UserUpdateProfileForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user)

    

    ctx = {
        'u_form': u_form,
        'p_form': p_form,
    }
    
    return render(request, 'auth/profile.html',ctx)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.UserProfile.save()

