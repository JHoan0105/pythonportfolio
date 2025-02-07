
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm #prebuilt form form django
from django.contrib.auth.models import User

# inherit UserCreationForm to extend
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    # change some of the parent properties of the class
    # needs to be Named Meta
    class Meta:
        model = User
        # show up on the form in the order that it appears here
        fields = ["username", "email", "password1", "password2"]
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already taken')
        return username