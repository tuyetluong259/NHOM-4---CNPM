from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from django.contrib import messages
from .models import Appointment

def home(request):
    return render(request,'KhachHang/home_KH.html')
"""def quan_ly_thu_cung(request):
    return render(request, 'quan_ly_thu_cung.html')
"""

def pet_list(request):
    """Hiển thị danh sách thú cưng"""
    pets = Appointment.objects.all()
    return render(request, 'KhachHang/pet_list.html', {'pets': pets})

def pet_detail(request, pet_id):
    """Hiển thị thông tin chi tiết thú cưng"""
    pet = get_object_or_404(Appointment, id=pet_id)
    return render(request, 'KhachHang/pet_detail.html', {'pet': pet})

def login(request):
    return render(request, 'home/login.html')
# Trang đăng ký khám bệnh
def dang_ky_kham_benh(request):
    if request.method == "POST":
        owner_name = request.POST.get("owner_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        address = request.POST.get("address")

        pet_name = request.POST.get("pet_name")
        pet_gender = request.POST.get("pet_gender")
        pet_condition = request.POST.get("pet_condition")

        appointment_date = request.POST.get("appointment_date")
        appointment_time = request.POST.get("appointment_time")

        doctor_name = request.POST.get("doctor_name")
        if doctor_name == "other":  # Nếu chọn "Bác sĩ khác"
            doctor_name = request.POST.get("doctor")  # Lấy tên bác sĩ nhập vào

        staff_notes = request.POST.get("staff_notes")

        # Lưu vào database
        appointment = Appointment(
            owner_name=owner_name,
            phone_number=phone_number,
            email=email,
            address=address,
            pet_name=pet_name,
            pet_gender=pet_gender,
            pet_condition=pet_condition,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            doctor_name=doctor_name,
            staff_notes=staff_notes,
        )
        appointment.save()

        # Hiển thị thông báo thành công
        messages.success(request, "Đăng ký khám bệnh thành công!")
        return redirect("dang_ky_kham_benh")  # Reload lại trang
    return render(request, "dang_ky_kham_benh.html")

# Trang đánh giá người dùng
def danh_gia_nguoi_dung(request):
    return render(request, 'danh_gia_nguoi_dung.html')

# Tài khoản
def giao_dien_khach_hang(request):
    return render(request, 'giao_dien_khach_hang.html')
    
# Trang thông tin khác - hiển thị danh sách lịch hẹn
def quan_ly_lich_hen(request):
    appointments = Appointment.objects.all()  # Lấy danh sách lịch hẹn
    
    if request.method == "POST":
        if "update_appointment" in request.POST:
            appointment_id = request.POST.get("appointment_id")
            appointment = get_object_or_404(Appointment, id=appointment_id)
            form = AppointmentForm(request.POST, instance=appointment)
            if form.is_valid():
                form.save()
                messages.success(request, "Cập nhật lịch hẹn thành công!")
            return redirect("quan_ly_lich_hen")

        elif "delete_appointment" in request.POST:
            print(request.POST)  # Kiểm tra dữ liệu gửi lên
            appointment_id = request.POST.get("appointment_id")
            appointment = get_object_or_404(Appointment, id=appointment_id)
            appointment.delete()
            messages.success(request, "Xóa lịch hẹn thành công!")
            return redirect("quan_ly_lich_hen")

    return render(request, 'quan_ly_lich_hen.html', {'appointments': appointments, 'form': AppointmentForm()})