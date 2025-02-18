from django.shortcuts import render, redirect
from .models import Registration
from .forms import RegistrationForm

def register_pet(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect('thank_you')  # Redirect to a thank-you page or confirmation page
    else:
        form = RegistrationForm()
    
    return render(request, 'dang_ky_kham_benh.html', {'form': form})

def home(request):
    return render(request,'KhachHang/home_KH.html')
def quan_ly_thu_cung(request):
    return render(request, 'quan_ly_thu_cung.html')

def login(request):
    return render(request, 'home/login.html')
# Trang đăng ký khám bệnh
def dang_ky_kham_benh(request):
    return render(request, 'dang_ky_kham_benh.html')

# Trang đánh giá người dùng
def danh_gia_nguoi_dung(request):
    return render(request, 'danh_gia_nguoi_dung.html')

# Trang thông tin khác
def thong_tin_khac(request):
    return render(request, 'thong_tin_khac.html')

# Tài khoản
def giao_dien_khach_hang(request):
    return render(request, 'giao_dien_khach_hang.html')
    

