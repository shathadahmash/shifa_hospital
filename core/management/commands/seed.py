from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import (
    Patient, Department, Room, Doctor, Nurse, Appointment,
    MedicalReport, Medicine, LabTest, Invoice, Payment
)
from datetime import date, time, timedelta


class Command(BaseCommand):
    help = "Insert sample data into hospital system"

    def handle(self, *args, **kwargs):
        Payment.objects.all().delete()
        Invoice.objects.all().delete()
        LabTest.objects.all().delete()
        Medicine.objects.all().delete()
        MedicalReport.objects.all().delete()
        Appointment.objects.all().delete()
        Nurse.objects.all().delete()
        Doctor.objects.all().delete()
        Room.objects.all().delete()
        Department.objects.all().delete()
        Patient.objects.all().delete()

        cardiology = Department.objects.create(name="Cardiology", description="Heart department")
        neurology = Department.objects.create(name="Neurology", description="Brain and nerves department")
        pediatrics = Department.objects.create(name="Pediatrics", description="Children department")
        emergency = Department.objects.create(name="Emergency", description="Emergency cases")

        Room.objects.create(room_number="101", room_type="General", is_available=True)
        Room.objects.create(room_number="102", room_type="Private", is_available=False)
        Room.objects.create(room_number="201", room_type="ICU", is_available=True)
        Room.objects.create(room_number="301", room_type="Surgery", is_available=True)

        doctor1 = Doctor.objects.create(
            full_name="Ahmed Hassan",
            specialization="Cardiologist",
            department=cardiology,
            phone="01011112222",
            email="ahmed@hospital.com",
            room_number="101",
            available=True
        )

        doctor2 = Doctor.objects.create(
            full_name="Sara Ali",
            specialization="Neurologist",
            department=neurology,
            phone="01033334444",
            email="sara@hospital.com",
            room_number="102",
            available=True
        )

        doctor3 = Doctor.objects.create(
            full_name="Mona Adel",
            specialization="Pediatrician",
            department=pediatrics,
            phone="01055556666",
            email="mona@hospital.com",
            room_number="201",
            available=False
        )

        Nurse.objects.create(full_name="Nour Mohamed", department=emergency, phone="01111112222", shift="Morning")
        Nurse.objects.create(full_name="Hana Mostafa", department=cardiology, phone="01133334444", shift="Night")
        Nurse.objects.create(full_name="Youssef Samir", department=neurology, phone="01155556666", shift="Evening")

        patient1 = Patient.objects.create(
            full_name="Omar Khaled",
            age=28,
            gender="Male",
            phone="01211112222",
            email="omar@email.com",
            address="Cairo",
            blood_group="O+",
            emergency_contact="01299998888"
        )

        patient2 = Patient.objects.create(
            full_name="Laila Mostafa",
            age=35,
            gender="Female",
            phone="01233334444",
            email="laila@email.com",
            address="Giza",
            blood_group="A+",
            emergency_contact="01277776666"
        )

        patient3 = Patient.objects.create(
            full_name="Yassin Ahmed",
            age=9,
            gender="Male",
            phone="01255556666",
            email="parent@email.com",
            address="Alexandria",
            blood_group="B+",
            emergency_contact="01244443333"
        )

        appointment1 = Appointment.objects.create(
            patient=patient1,
            doctor=doctor1,
            date=date.today(),
            time=time(10, 30),
            status="Pending",
            reason="Chest pain",
            notes="Needs ECG check"
        )

        appointment2 = Appointment.objects.create(
            patient=patient2,
            doctor=doctor2,
            date=date.today() + timedelta(days=1),
            time=time(12, 0),
            status="Completed",
            reason="Headache",
            notes="Follow-up required"
        )

        appointment3 = Appointment.objects.create(
            patient=patient3,
            doctor=doctor3,
            date=date.today() + timedelta(days=2),
            time=time(9, 0),
            status="Cancelled",
            reason="Fever",
            notes="Cancelled by patient"
        )

        MedicalReport.objects.create(
            patient=patient1,
            doctor=doctor1,
            appointment=appointment1,
            diagnosis="Mild chest discomfort",
            prescription="Pain relief medication",
            treatment="Rest and ECG test",
            notes="Monitor blood pressure"
        )

        MedicalReport.objects.create(
            patient=patient2,
            doctor=doctor2,
            appointment=appointment2,
            diagnosis="Migraine",
            prescription="Migraine tablets",
            treatment="Avoid stress and bright light",
            notes="Review after 2 weeks"
        )

        Medicine.objects.create(name="Paracetamol", quantity=200, price=15.00, expiry_date=date.today() + timedelta(days=365))
        Medicine.objects.create(name="Amoxicillin", quantity=120, price=45.00, expiry_date=date.today() + timedelta(days=240))
        Medicine.objects.create(name="Ibuprofen", quantity=90, price=30.00, expiry_date=date.today() + timedelta(days=180))

        LabTest.objects.create(
            patient=patient1,
            test_name="Blood Test",
            result="Normal"
        )

        LabTest.objects.create(
            patient=patient2,
            test_name="MRI Scan",
            result="No serious issue found"
        )

        invoice1 = Invoice.objects.create(
            patient=patient1,
            amount=750.00,
            status="Paid"
        )

        invoice2 = Invoice.objects.create(
            patient=patient2,
            amount=1200.00,
            status="Unpaid"
        )

        Payment.objects.create(
            invoice=invoice1,
            amount=750.00,
            payment_method="Cash"
        )

        Payment.objects.create(
            invoice=invoice2,
            amount=500.00,
            payment_method="Card"
        )

        self.stdout.write(self.style.SUCCESS("Sample hospital data inserted successfully."))