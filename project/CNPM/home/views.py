import json
import traceback
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.contrib.admin.views.decorators import staff_member_required
from .models import Revenue

# Trang chủ
def home(request):
    return render(request, "home/home.html")

def index(request):
    return render(request, "home/index.html")

# Đăng nhập
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body) if request.content_type.startswith("application/json") else request.POST
        email, password, role = data.get("email"), data.get("password"), data.get("role")

        if not email or not password:
            return JsonResponse({"success": False, "message": "Thiếu email hoặc mật khẩu!"}, status=400)

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({"success": False, "message": "Sai email hoặc mật khẩu!"}, status=401)

        user = authenticate(request, username=user_obj.username, password=password)
        if user:
            auth_login(request, user)

            # Điều hướng theo vai trò
            redirect_url = "/myadmin/" if user.is_superuser else {
                "bacsi": "/homeBS/",
                "nhanvien": "/homeNV/",
                "khachhang": "/homeKH/"
            }.get(role, "/")

            return JsonResponse({"success": True, "redirect_url": redirect_url})

        return JsonResponse({"success": False, "message": "Sai email hoặc mật khẩu!"}, status=401)

    return render(request, "home/login.html")

# Đăng ký
@csrf_exempt
def register_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body) if request.content_type.startswith("application/json") else request.POST
            email, password = data.get("email"), data.get("password")

            if not email or not password:
                return JsonResponse({"success": False, "message": "Thiếu email hoặc mật khẩu!"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"success": False, "message": "Email đã tồn tại!"}, status=400)

            user = User.objects.create_user(username=email, email=email, password=password)
            khachhang_group, _ = Group.objects.get_or_create(name="khachhang")
            user.groups.add(khachhang_group)

            return JsonResponse({"success": True, "redirect_url": "/login/"})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e), "trace": traceback.format_exc()}, status=500)

    return JsonResponse({"success": False, "message": "Phương thức không hợp lệ!"}, status=405)

# Admin Views
@staff_member_required
def myadmin_view(request):
    return render(request, "admin/myadmin.html")

@staff_member_required
def revenue_dashboard(request):
    return render(request, "home/admin/revenue-dashboard.html")

@require_GET
@staff_member_required
def revenue_api(request):
    revenues = Revenue.objects.order_by("date")
    data = {"dates": [r.date.strftime("%Y-%m-%d") for r in revenues], "amounts": [float(r.amount) for r in revenues]}
    return JsonResponse(data)

# Trang theo vai trò
@login_required
def homeBS(request):
    return render(request, "home/homeBS.html")

@login_required
def homeKH(request):
    return render(request, "home/homeKH.html")

@login_required
def homeNV(request):
    return render(request, "home/homeNV.html")

# Các trang khác (render động)
def render_template(request, template_name):
    return render(request, f"home/{template_name}.html")

template_views = [
    "thucan", "bookings", "chi_tiet_thu_cung", "dang_ky_kham_benh", "danh_gia_nguoi_dung", 
    "edit_medical", "giao_dien_khach_hang", "inpatient_care", "pets", "quan_ly_thu_cung", 
    "record_medical", "rooms", "schedule"
]

for view_name in template_views:
    globals()[view_name] = lambda request, name=view_name: render_template(request, name)
