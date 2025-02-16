import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import Revenue

def home(request):
    return render(request, 'home/home.html')
def register(request):
    return render(request, 'home/register.html')
def login_view(request):
    if request.method == "POST":
        # Nếu request đến từ form HTML bình thường
        if request.content_type == "application/x-www-form-urlencoded":
            email = request.POST.get("email")
            password = request.POST.get("password")
        else:
            # Nếu request đến từ fetch API
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

        try:
            # Lấy user từ email thay vì username
            user = User.objects.get(email=email)
            # Thực hiện xác thực với email đã tìm được
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            # Đăng nhập thành công
            auth_login(request, user)
            
            if user.is_superuser:
                # Chuyển hướng đến trang admin nếu là admin
                if request.content_type == "application/json":
                    return JsonResponse({"success": True, "redirect_url": "/admin/"})
                else:
                    return redirect("/admin/")
            else:
                # Chuyển hướng khi dùng form truyền thống
                if user.groups.filter(name="bacsi").exists():
                    return redirect('homeBS')
                elif user.groups.filter(name="nhanvien").exists():
                    return redirect('homeNV')
                elif user.groups.filter(name="khachhang").exists():
                    return redirect('homeKH')
                else:
                    return redirect('home')  # Trang chủ nếu không thuộc nhóm nào

        else:
            # Đăng nhập thất bại
            if request.content_type == "application/json":
                return JsonResponse({"success": False, "message": "Sai email hoặc mật khẩu!"}, status=401)
            else:
                return render(request, 'home/login.html', {"error": "Sai email hoặc mật khẩu!"})

    return render(request, 'home/login.html')
def register_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return JsonResponse({"success": False, "message": "Thiếu email hoặc mật khẩu!"}, status=400)

        if User.objects.filter(username=email).exists():
            return JsonResponse({"success": False, "message": "Email đã tồn tại!"}, status=400)

        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        return JsonResponse({"success": True, "message": "Đăng ký thành công!"})

    return JsonResponse({"success": False, "message": "Phương thức không hợp lệ!"}, status=405)

@login_required
def homeBS(request):
    return render(request, 'home/homeBS.html')

@login_required
def homeKH(request):
    return render(request, 'home/homeKH.html')

@login_required
def homeNV(request):
    return render(request, 'home/homeNV.html')

# Các trang khác giữ nguyên

def thucan(request):
    return render(request, 'home/thucan.html')

def bookings(request):
    return render(request, 'home/bookings.html')

def chi_tiet_thu_cung(request):
    return render(request, 'home/chi_tiet_thu_cung.html')

def dang_ky_kham_benh(request):
    return render(request, 'home/dang_ky_kham_benh.html')

def danh_gia_nguoi_dung(request):
    return render(request, 'home/danh_gia_nguoi_dung.html')

def edit_medical(request):
    return render(request, 'home/edit_medical.html')

def giao_dien_khach_hang(request):
    return render(request, 'home/giao_dien_khach_hang.html')

def index(request):
    return render(request, 'home/index.html')

def inpatient_care(request):
    return render(request, 'home/inpatient_care.html')

def pets(request):
    return render(request, 'home/pets.html')

def quan_ly_thu_cung(request):
    return render(request, 'home/quan_ly_thu_cung.html')

def record_medical(request):
    return render(request, 'home/record_medical.html')

def rooms(request):
    return render(request, 'home/rooms.html')

def schedule(request):
    return render(request, 'home/schedule.html')

# API doanh thu
def revenue_api(request):
    revenues = Revenue.objects.order_by('date')
    data = {
        "dates": [r.date.strftime("%Y-%m-%d") for r in revenues],
        "amounts": [float(r.amount) for r in revenues]
    }
    return JsonResponse(data)
