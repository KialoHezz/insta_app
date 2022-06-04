from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ('username','email')


class UpdateProfileForm(forms.ModelForm):
    class Meta :
        model = UserProfile
        fields = ('photo','bio')
        

class UserUpdateProfileForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email')




