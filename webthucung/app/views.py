from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
    return render(request,'app/home.html')
def quan_ly_thu_cung(request):
    return render(request, 'quan_ly_thu_cung.html')

# Trang chi tiết thú cưng
def chi_tiet_thu_cung(request):
    return render(request, 'chi_tiet_thu_cung.html')

# Trang đăng ký khám bệnh
def dang_ky_kham_benh(request):
    return render(request, 'dang_ky_kham_benh.html')

# Trang đánh giá người dùng
def danh_gia_nguoi_dung(request):
    return render(request, 'danh_gia_nguoi_dung.html')

# Trang thông tin khác
def thong_tin_khac(request):
    return render(request, 'thong_tin_khac.html')

