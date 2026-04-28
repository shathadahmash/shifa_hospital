from django.contrib import admin
from .models import (
    Patient,
    Department,
    Room,
    Doctor,
    Nurse,
    Appointment,
    MedicalReport,
    Medicine,
    LabTest,
    Invoice,
    Payment,
)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "age", "gender", "phone", "blood_group", "created_at")
    search_fields = ("full_name", "phone", "email")
    list_filter = ("gender", "blood_group", "created_at")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("room_number", "room_type", "is_available")
    search_fields = ("room_number", "room_type")
    list_filter = ("room_type", "is_available")


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "specialization", "department", "phone", "available")
    search_fields = ("full_name", "specialization", "phone")
    list_filter = ("department", "specialization", "available")


@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ("full_name", "department", "phone", "shift")
    search_fields = ("full_name", "phone", "shift")
    list_filter = ("department", "shift")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "date", "time", "status")
    search_fields = ("patient__full_name", "doctor__full_name")
    list_filter = ("status", "date", "doctor")


@admin.register(MedicalReport)
class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "created_at")
    search_fields = ("patient__full_name", "doctor__full_name", "diagnosis")
    list_filter = ("doctor", "created_at")


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "price", "expiry_date")
    search_fields = ("name",)
    list_filter = ("expiry_date",)


@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ("patient", "test_name", "test_date")
    search_fields = ("patient__full_name", "test_name", "result")
    list_filter = ("test_date",)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "amount", "status", "created_at")
    search_fields = ("patient__full_name",)
    list_filter = ("status", "created_at")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "invoice", "amount", "payment_method", "paid_at")
    search_fields = ("invoice__patient__full_name", "payment_method")
    list_filter = ("payment_method", "paid_at")