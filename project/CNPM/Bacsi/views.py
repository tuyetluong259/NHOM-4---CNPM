from django.shortcuts import render, get_object_or_404, redirect
from .models import MedicalRecord
from Nhanvien.models import Booking

# Danh sách MedicalRecord
def list_Bacsi(request):
    records = MedicalRecord.objects.distinct()  # Tránh lấy dữ liệu trùng
    return render(request, "Bacsi/list.html", {"records": records})

def medical_records(request):
    records = MedicalRecord.objects.all()  # Lấy danh sách hồ sơ bệnh án
    return render(request, 'Bacsi/medical_records.html', {'records': records})
# Xem chi tiết MedicalRecord
def Bacsi_detail(request, record_id):
    record = get_object_or_404(MedicalRecord, id=record_id)
    return render(request, "Bacsi/detail.html", {"record": record})
from django.shortcuts import render, get_object_or_404, redirect
from .models import MedicalRecord

def inpatient_care(request):
    records = MedicalRecord.objects.filter(status="NHAP_VIEN").select_related("booking")

    if request.method == "POST":
        record_id = request.POST.get("record_id")
        cage_number = request.POST.get("cage_number")
        status = request.POST.get("status")
        notes = request.POST.get("notes")
        diagnosis = request.POST.get("diagnosis")
        prescription = request.POST.get("prescription")

        record = get_object_or_404(MedicalRecord, id=record_id)

        # Cập nhật thông tin
        if cage_number:
            record.cage_number = cage_number
        if status:
            record.status = status
        if notes:
            record.notes = notes
        if diagnosis:
            record.diagnosis = diagnosis
        if prescription:
            record.prescription = prescription

        record.save()

        return redirect("inpatient_care")  # Reload trang

    return render(request, "Bacsi/inpatient_care.html", {"records": records})

# Tạo mới MedicalRecord
def create_Bacsi(request):
    if request.method == "POST":
        booking_id = request.POST.get("booking_id")
        doctor_name = request.POST.get("doctor_name")
        booking = get_object_or_404(Booking, id=booking_id)
        MedicalRecord.objects.create(booking=booking, doctor_name=doctor_name)
        return redirect("list_Bacsi")
    return render(request, "Bacsi/create.html")

# Cập nhật MedicalRecord

def update_Bacsi(request, record_id):
    record = get_object_or_404(MedicalRecord, id=record_id)

    if request.method == "POST":
        doctor_name = request.POST.get("doctor_name")
        diagnosis = request.POST.get("diagnosis")
        prescription = request.POST.get("prescription")
        notes = request.POST.get("notes")
        status = request.POST.get("status")  # ✅ Lấy giá trị trạng thái từ form

        # Debug: Kiểm tra dữ liệu nhận được
        print(f"Received data - Doctor: {doctor_name}, Status: {status}, Diagnosis: {diagnosis}")

        # Cập nhật thông tin vào database
        record.doctor_name = doctor_name
        record.diagnosis = diagnosis
        record.prescription = prescription
        record.notes = notes
        record.status = status  # ✅ Cập nhật trạng thái
        record.save()

        # Debug: Kiểm tra lại trong database
        print(f"Updated MedicalRecord {record.id} - Status: {record.status}")

        return redirect("Bacsi_detail", record_id=record.id)  

    return render(request, "Bacsi/update.html", {"record": record})

# Xóa MedicalRecord
def delete_Bacsi(request, record_id):
    record = get_object_or_404(MedicalRecord, id=record_id)
    record.delete()
    return redirect("list_Bacsi")

# Sửa hồ sơ khám bệnh
def edit_medical(request, record_id):
    pet = get_object_or_404(MedicalRecord, id=record_id)
    if request.method == 'POST':
        pet.name = request.POST.get('name')
        pet.species = request.POST.get('species')
        pet.progress = request.POST.get('progress')
        pet.save()
        return redirect('inpatient_care')

    return render(request, 'Bacsi/edit_medical.html', {'pet': pet})

# Xóa hồ sơ khám bệnh
def delete_medical(request, record_id):
    pet = get_object_or_404(MedicalRecord, id=record_id)
    pet.delete()
    return redirect('inpatient_care')

# Đăng nhập
def login_view(request):
    return render(request, 'home/login.html')
# Trang chủ
def home(request):
    context = {}
    return render(request, 'Bacsi/home.html', context)
