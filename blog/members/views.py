from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import AccessMixin
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms
from base.models import Profile

# Mixins

class UnloginRequiredMixin(AccessMixin):
    """
    Faqat autentifikatsiyadan o'tmagan foydalanuvchilarga kirishga ruxsat beruvchi mixin.
    Agar foydalanuvchi allaqachon autentifikatsiyadan o'tgan bo'lsa, u 'home' sahifasiga yo'naltiriladi.
    """
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
# Mixins


class UserRegisterView(UnloginRequiredMixin, generic.CreateView):
    form_class = forms.SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('add_profile')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

class UserLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'  # Login shabloni
    form_class = forms.LoginForm  # Maxsus forma klassi
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        print("Form is valid!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Form is invalid!")
        return super().form_invalid(form)

class UserEditView(LoginRequiredMixin, generic.UpdateView):
    form_class = forms.EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    form_class = forms.UpdateProfileForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile
    
class UserProfileView(LoginRequiredMixin, generic.DetailView):
    template_name = 'profile.html'

    def get_object(self):
        return self.request.user
    
class SuccessPasswordView(LoginRequiredMixin, auth_views.PasswordChangeDoneView):
    template_name = 'success_password.html'

    
class ChangePasswordView(LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'change_password.html'
    form_class = forms.ChangePasswordForm
    success_url = reverse_lazy('success_password')


