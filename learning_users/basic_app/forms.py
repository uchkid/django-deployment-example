from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(UserCreationForm):    
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site', 'profile_pic')