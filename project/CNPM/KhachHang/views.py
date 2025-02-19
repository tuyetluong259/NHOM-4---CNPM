from django.shortcuts import render, redirect
from .forms import LichHenForm
from django.contrib import messages
from .models import KhachHang, LichHen, ThuCung


def home(request):
    return render(request,'KhachHang/home_KH.html')
def quan_ly_thu_cung(request):
    return render(request, 'quan_ly_thu_cung.html')

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
        staff_notes = request.POST.get("staff_notes")

        # Kiểm tra xem khách hàng đã tồn tại chưa
        khach_hang, created = KhachHang.objects.get_or_create(
            email=email,
            defaults={
                "owner_name": owner_name,
                "phone_number": phone_number,
                "address": address
            }
        )

        # Nếu khách hàng đã tồn tại, cập nhật thông tin (nếu cần)
        if not created:
            khach_hang.owner_name = owner_name
            khach_hang.phone_number = phone_number
            khach_hang.address = address
            khach_hang.save()

        # Thêm thú cưng vào hệ thống
        thu_cung = ThuCung.objects.create(
            pet_name=pet_name,
            pet_gender=pet_gender,
            pet_condition=pet_condition,
            owner=khach_hang
        )

        # Tạo lịch hẹn
        LichHen.objects.create(
            khach_hang=khach_hang,
            thu_cung=thu_cung,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            doctor_name=doctor_name,
            staff_notes=staff_notes
        )

        messages.success(request, "Đăng ký thành công! Vui lòng chờ xác nhận từ nhân viên.")
        return redirect("dang_ky_kham_benh")  # Quay lại trang sau khi đăng ký

    return render(request, "dang_ky_kham_benh.html")

# Trang đánh giá người dùng
def danh_gia_nguoi_dung(request):
    return render(request, 'danh_gia_nguoi_dung.html')

# Trang thông tin khác
def thong_tin_khac(request):
    return render(request, 'thong_tin_khac.html')

# Tài khoản
def giao_dien_khach_hang(request):
    return render(request, 'giao_dien_khach_hang.html')
    

