from django import forms
from .models import Weepitch
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class WeepitchForm(forms.ModelForm):
    class Meta:
        model = Weepitch
        fields = ['text','photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.is_active = True
        user.save() 
        return user