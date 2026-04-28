from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("dashboard/", views.dashboard_redirect, name="dashboard"),

    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/receptionist/", views.receptionist_dashboard, name="receptionist_dashboard"),
    path("dashboard/doctor/", views.doctor_dashboard, name="doctor_dashboard"),
    path("dashboard/nurse/", views.nurse_dashboard, name="nurse_dashboard"),

    path("patients/", views.patients_list, name="patients_list"),
    path("appointments/", views.appointments_list, name="appointments_list"),
    path("reports/", views.reports_list, name="reports_list"),
    path("invoices/", views.invoices_list, name="invoices_list"),
    path("patients/", views.patients_list, name="patients_list"),
    path("patients/<int:pk>/edit/", views.patient_edit, name="patient_edit"),
    path("appointments/", views.appointments_list, name="appointments_list"),
    path("appointments/<int:pk>/edit/", views.appointment_edit, name="appointment_edit"),
    path("appointments/<int:pk>/delete/", views.appointment_delete, name="appointment_delete"),
    path("invoices/", views.invoices_list, name="invoices_list"),
    path("invoices/<int:pk>/edit/", views.invoice_edit, name="invoice_edit"),
    path("invoices/<int:pk>/delete/", views.invoice_delete, name="invoice_delete"),
    
]