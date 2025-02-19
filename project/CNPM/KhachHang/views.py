from django.shortcuts import render, redirect
from .forms import KhachHangForm, ThuCungForm, LichHenForm
from django.contrib import messages
from .models import KhachHang, LichHen, ThuCung, BacSi

def dat_lich_hen(request):
    if request.method == 'POST':
        form = LichHenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_lich_hen')  # Chuyển hướng sau khi lưu
    else:
        form = LichHenForm()
    
    return render(request, 'dat_lich_hen.html', {'form': form})

def danh_sach_lich_hen(request):
    lich_hen_list = LichHen.objects.all()
    return render(request, 'danh_sach_lich_hen.html', {'lich_hen_list': lich_hen_list})

def home(request):
    return render(request,'KhachHang/home_KH.html')
def quan_ly_thu_cung(request):
    return render(request, 'quan_ly_thu_cung.html')

def login(request):
    return render(request, 'home/login.html')
# Trang đăng ký khám bệnh
def dang_ky_kham_benh(request):
    if request.method == "POST":
        # Khởi tạo form với dữ liệu POST
        khach_hang_form = KhachHangForm(request.POST)
        thu_cung_form = ThuCungForm(request.POST)
        lich_hen_form = LichHenForm(request.POST)

        if khach_hang_form.is_valid() and thu_cung_form.is_valid() and lich_hen_form.is_valid():
            # Lưu thông tin khách hàng
            khach_hang = khach_hang_form.save()

            # Lưu thông tin thú cưng
            thu_cung = thu_cung_form.save(commit=False)
            thu_cung.owner = khach_hang
            thu_cung.save()

            # Lưu lịch hẹn
            lich_hen = lich_hen_form.save(commit=False)
            lich_hen.khach_hang = khach_hang
            lich_hen.thu_cung = thu_cung
            lich_hen.save()

            messages.success(request, "Đăng ký thành công! Vui lòng chờ xác nhận từ nhân viên.")
            return redirect("dang_ky_kham_benh")  # Quay lại trang sau khi đăng ký
        else:
            messages.error(request, "Đã xảy ra lỗi. Vui lòng kiểm tra lại thông tin.")
    else:
        # Khởi tạo form trống
        khach_hang_form = KhachHangForm()
        thu_cung_form = ThuCungForm()
        lich_hen_form = LichHenForm()

    return render(request, "dang_ky_kham_benh.html", {
        'khach_hang_form': khach_hang_form,
        'thu_cung_form': thu_cung_form,
        'lich_hen_form': lich_hen_form,
        'bac_si_list': BacSi.objects.all(),
    })
# Trang đánh giá người dùng
def danh_gia_nguoi_dung(request):
    return render(request, 'danh_gia_nguoi_dung.html')

# Trang thông tin khác
def thong_tin_khac(request):
    return render(request, 'thong_tin_khac.html')

# Tài khoản
def giao_dien_khach_hang(request):
    return render(request, 'giao_dien_khach_hang.html')
    
