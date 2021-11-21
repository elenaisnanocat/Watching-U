from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['username',]


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['description', 'image',]