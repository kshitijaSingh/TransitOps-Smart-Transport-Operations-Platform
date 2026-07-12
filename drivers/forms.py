from django import forms
from .models import Driver


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["name", "license_number", "license_category", "license_expiry", "phone_number", "safety_score", "status"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "license_number": forms.TextInput(attrs={"class": "form-control"}),
            "license_category": forms.TextInput(attrs={"class": "form-control"}),
            "license_expiry": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "safety_score": forms.NumberInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }
