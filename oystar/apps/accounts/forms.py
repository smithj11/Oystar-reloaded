from oystar.apps.accounts.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms.models import ModelForm


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=60, required=True, help_text="Add valid email address")
    full_name = forms.CharField(label='full_name', required=True, max_length=100)
    # password = forms.CharField(widget=forms.PasswordInput)
    # password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    template = 'accounts/register.html'
    class Meta:
        model = CustomUser
        print(model)
        fields =("email", "full_name", "password1", "password2")
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.full_name = self.cleaned_data['full_name']
        print(user.full_name)

        if commit:
            user.save()
            print(user)

        return user
    


class LoginForm(AuthenticationForm):
    template='accounts/login.html'
    username= forms.CharField(label='Email ')
    model = get_user_model()