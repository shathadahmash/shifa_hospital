from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Patient, Doctor, Appointment, MedicalReport, Invoice
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Patient, Doctor, Appointment, MedicalReport, Invoice
from .forms import PatientForm


def home(request):
    return render(request, "core/home.html")


def is_admin(user):
    return user.is_superuser or user.groups.filter(name="Admin").exists()


def is_receptionist(user):
    return user.groups.filter(name="Receptionist").exists()


def is_doctor(user):
    return user.groups.filter(name="Doctor").exists()


def is_nurse(user):
    return user.groups.filter(name="Nurse").exists()


@login_required
def dashboard_redirect(request):
    user = request.user

    if is_admin(user):
        return redirect("admin_dashboard")

    if is_receptionist(user):
        return redirect("receptionist_dashboard")

    if is_doctor(user):
        return redirect("doctor_dashboard")

    if is_nurse(user):
        return redirect("nurse_dashboard")

    return redirect("login")


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    context = {
        "patients_count": Patient.objects.count(),
        "doctors_count": Doctor.objects.count(),
        "appointments_count": Appointment.objects.count(),
        "invoices_count": Invoice.objects.count(),
        "recent_appointments": Appointment.objects.select_related("patient", "doctor")[:5],
    }
    return render(request, "core/admin_dashboard.html", context)


@login_required
@user_passes_test(is_receptionist)
def receptionist_dashboard(request):
    context = {
        "patients_count": Patient.objects.count(),
        "appointments_count": Appointment.objects.count(),
        "invoices_count": Invoice.objects.count(),
        "recent_appointments": Appointment.objects.select_related("patient", "doctor")[:5],
    }
    return render(request, "core/receptionist_dashboard.html", context)


@login_required
@user_passes_test(is_doctor)
def doctor_dashboard(request):
    context = {
        "appointments_count": Appointment.objects.count(),
        "reports_count": MedicalReport.objects.count(),
        "recent_appointments": Appointment.objects.select_related("patient", "doctor")[:5],
    }
    return render(request, "core/doctor_dashboard.html", context)


@login_required
@user_passes_test(is_nurse)
def nurse_dashboard(request):
    context = {
        "patients_count": Patient.objects.count(),
        "appointments_count": Appointment.objects.count(),
        "recent_appointments": Appointment.objects.select_related("patient", "doctor")[:5],
    }
    return render(request, "core/nurse_dashboard.html", context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient
from .forms import PatientForm


@login_required
def patients_list(request):
    patients = Patient.objects.all()
    form = PatientForm()

    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patients_list")

    return render(request, "core/patients_list.html", {
        "patients": patients,
        "form": form,
    })


@login_required
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect("patients_list")

    return redirect("patients_list")
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment, Patient, Doctor
from .forms import AppointmentForm


@login_required
def appointments_list(request):
    appointments = Appointment.objects.select_related("patient", "doctor").all()
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("appointments_list")
    else:
        form = AppointmentForm()

    return render(request, "core/appointments_list.html", {
        "appointments": appointments,
        "patients": patients,
        "doctors": doctors,
        "form": form,
    })


@login_required
def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()

    return redirect("appointments_list")


@login_required
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    if request.method == "POST":
        appointment.delete()

    return redirect("appointments_list")


@login_required
def reports_list(request):
    reports = MedicalReport.objects.select_related("patient", "doctor").all()
    return render(request, "core/reports_list.html", {"reports": reports})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Invoice, Patient
from .forms import InvoiceForm


@login_required
def invoices_list(request):
    invoices = Invoice.objects.select_related("patient").all()
    patients = Patient.objects.all()

    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("invoices_list")
    else:
        form = InvoiceForm()

    return render(request, "core/invoices_list.html", {
        "invoices": invoices,
        "patients": patients,
        "form": form,
    })


@login_required
def invoice_edit(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)

    if request.method == "POST":
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()

    return redirect("invoices_list")


@login_required
def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)

    if request.method == "POST":
        invoice.delete()

    return redirect("invoices_list")

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_user(request):
    logout(request)
    return redirect("home")