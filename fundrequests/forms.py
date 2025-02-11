from django import forms
from .models import Fundraiser

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
