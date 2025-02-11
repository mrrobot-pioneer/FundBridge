from django import forms
from .models import Fundraiser
from django.contrib.auth.models import User

class FundraiserForm(forms.ModelForm):
    class Meta:
        model = Fundraiser
        fields = ["title", "description", "category", "image", "target_amount"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter a compelling title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Tell your story..."}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "target_amount": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Set a goal amount"}),
        }


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"}),
        min_length=8,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm password"}),
        min_length=8,
    )

    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email"}),
        }

    def clean_password2(self):
        """Ensure both passwords match"""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")
        return password2


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
    )