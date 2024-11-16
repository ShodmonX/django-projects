from django import forms

from django_ckeditor_5.fields import CKEditor5Field
from django_ckeditor_5 import widgets as ck_widgets

from . import models


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = models.Profile
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

class CreatePostForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=models.Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'})
    )
    body = CKEditor5Field('Body')
    class Meta:
        model = models.Post
        fields = ['title', 'title_tag', 'category', 'body', 'header_image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }


class EditPostForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=models.Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'})
    )
    body = CKEditor5Field('Body')
    class Meta:
        model = models.Post
        fields = ['title', 'title_tag', 'category', 'body', 'header_image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


