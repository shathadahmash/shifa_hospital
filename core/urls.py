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
]