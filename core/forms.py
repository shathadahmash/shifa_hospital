from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "full_name",
            "age",
            "gender",
            "phone",
            "email",
            "address",
            "blood_group",
            "emergency_contact",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "input", "placeholder": "Full name"}),
            "age": forms.NumberInput(attrs={"class": "input", "placeholder": "Age"}),
            "gender": forms.Select(attrs={"class": "input"}),
            "phone": forms.TextInput(attrs={"class": "input", "placeholder": "Phone"}),
            "email": forms.EmailInput(attrs={"class": "input", "placeholder": "Email"}),
            "address": forms.Textarea(attrs={"class": "input", "rows": 3, "placeholder": "Address"}),
            "blood_group": forms.Select(attrs={"class": "input"}),
            "emergency_contact": forms.TextInput(attrs={"class": "input", "placeholder": "Emergency contact"}),
        }