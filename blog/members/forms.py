from django.contrib.auth import forms as auth_forms
from django.contrib.auth import models as auth_models
from django import forms

from base.models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your username'
        }),
        label='Username',
        max_length=150,
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        }),
        label='Password',
        required=True
    )


class SignUpForm(auth_forms.UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Firstname'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Lastname'}))
    class Meta:
        model = auth_models.User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Create username'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'


class EditProfileForm(auth_forms.UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Firstname'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Lastname'}))
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Firstname'}))
    class Meta:
        model = auth_models.User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image', 'telegram_url', 'instagram_url', 'facebook_url', 'twitter_url', 'website_url']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'telegram_url': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'instagram_url': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'facebook_url': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'twitter_url': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'website_url': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


class ChangePasswordForm(auth_forms.PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your old passwaord', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create new password', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password', 'type': 'password'}))
    class Meta:
        model = auth_models.User
        fields = ['old_password', 'new_password1', 'new_password2']