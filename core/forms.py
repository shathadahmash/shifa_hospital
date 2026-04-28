from django import forms
from .models import Patient, Appointment
from .models import Invoice

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
            "full_name": forms.TextInput(attrs={
                "class": "input",
                "placeholder": "Full name"
            }),

            "age": forms.NumberInput(attrs={
                "class": "input",
                "placeholder": "Age"
            }),

            "gender": forms.Select(attrs={
                "class": "input"
            }),

            "phone": forms.TextInput(attrs={
                "class": "input",
                "placeholder": "Phone"
            }),

            "email": forms.EmailInput(attrs={
                "class": "input",
                "placeholder": "Email"
            }),

            "address": forms.Textarea(attrs={
                "class": "input",
                "rows": 3,
                "placeholder": "Address"
            }),

            "blood_group": forms.Select(attrs={
                "class": "input"
            }),

            "emergency_contact": forms.TextInput(attrs={
                "class": "input",
                "placeholder": "Emergency contact"
            }),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "patient",
            "doctor",
            "date",
            "time",
            "reason",
            "status",
            "notes",
        ]

        widgets = {
            "patient": forms.Select(attrs={
                "class": "input"
            }),

            "doctor": forms.Select(attrs={
                "class": "input"
            }),

            "date": forms.DateInput(attrs={
                "class": "input",
                "type": "date"
            }),

            "time": forms.TimeInput(attrs={
                "class": "input",
                "type": "time"
            }),

            "reason": forms.TextInput(attrs={
                "class": "input",
                "placeholder": "Reason for visit"
            }),

            "status": forms.Select(attrs={
                "class": "input"
            }),

            "notes": forms.Textarea(attrs={
                "class": "input",
                "rows": 3,
                "placeholder": "Notes"
            }),
        }




class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ["patient", "amount", "status"]

        widgets = {
            "patient": forms.Select(attrs={"class": "input"}),
            "amount": forms.NumberInput(attrs={
                "class": "input",
                "placeholder": "Amount",
                "step": "0.01"
            }),
            "status": forms.Select(attrs={"class": "input"}),
        }