from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.dispatch import receiver

from .forms import UserRegisterForm,UpdateProfileForm
from .models import UserProfile,ImageIn
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
        
        p_form = UpdateProfileForm(request.POST,request.FILES, instance=request.user)

        if p_form.is_valid():
            p_form.save()

    

            messages.success(request,f"Your profile has been updated")

            return redirect('profile')

    else:
       
        p_form = UpdateProfileForm(instance=request.user)

    form = UpdateProfileForm()

    ctx = {
        'p_form': p_form,
        'form': form,
    }
    
    return render(request, 'auth/profile.html',ctx)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.UserProfile.save()

def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        dat = ''

        search_term = request.GET.get('search')

        search_searchies = ImageIn(search_term)


        messages = f'{search_term}'

    else:
        messages = "You have't searched for any term"

    return render(request, 'home/search.html', {'messages':messages})