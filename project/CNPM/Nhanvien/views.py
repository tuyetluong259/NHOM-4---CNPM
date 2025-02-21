from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking, PetHospitalization, DoctorSchedule, Room
from .forms import BookingForm

# Trang chủ Nhân viên
def home_NV(request):
    return render(request, 'Nhanvien/home_NV.html')

"""# Quản lý đặt lịch khám (Booking)
def booking(request):
    bookings = Booking.objects.all()  # Lấy tất cả các bản ghi đặt lịch
    return render(request, 'Nhanvien/booking.html', {'bookings': bookings})

# Thêm mới đặt lịch khám
def add_booking(request):
    if request.method == 'POST':
        # Lấy thông tin từ form
        pet_name = request.POST.get('pet_name')
        owner_name = request.POST.get('owner_name')
        appointment_date = request.POST.get('appointment_date')

        # Tạo một bản ghi đặt lịch mới
        booking = Booking(pet_name=pet_name, owner_name=owner_name, appointment_date=appointment_date)
        booking.save()  # Lưu vào cơ sở dữ liệu

        return redirect('booking')  # Quay lại trang danh sách đặt lịch

    return render(request, 'Nhanvien/add_booking.html')"""

def pet(request): 
    pets = Booking.objects.filter(status='NHAP_VIEN')  # Chỉ lấy thú cưng đang nhập viện
    
    if request.method == "POST":
        pet_id = request.POST.get("pet_id")  # Lấy ID thú cưng từ form
        pet = get_object_or_404(Booking, id=pet_id)
        form = BookingForm(request.POST, instance=pet)

        if form.is_valid():
            form.save()
            return redirect('pet')  # Quay lại danh sách sau khi cập nhật thành công
    else:
        form = BookingForm()

    return render(request, 'Nhanvien/pet.html', {'pets': pets, 'form': form})

def list_bookings(request):
    bookings = Booking.objects.all().order_by("-created_at")  # Sắp xếp mới nhất lên đầu
    return render(request, "Nhanvien/booking.html", {"bookings": bookings})

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    # Xử lý hủy booking
    booking.delete()

    return redirect("booking")
# Quản lý lịch khám của bác sĩ (Doctor Schedule)
def schedule(request):
    schedules = DoctorSchedule.objects.all()
    return render(request, 'Nhanvien/schedule.html', {'schedules': schedules})

# Thêm mới lịch khám của bác sĩ
def add_schedule(request):
    if request.method == 'POST':
        # Lấy thông tin từ form
        doctor_name = request.POST.get('doctor_name')
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Tạo một lịch khám mới
        schedule = DoctorSchedule(doctor_name=doctor_name, date=date, time=time)
        schedule.save()

        return redirect('schedule')

    return render(request, 'Nhanvien/add_schedule.html')

# Quản lý thú cưng nhập viện (Pet Hospitalization)

# Thêm mới hồ sơ nhập viện cho thú cưng
def add_pet(request):
    if request.method == 'POST':
        # Lấy thông tin từ form
        pet_name = request.POST.get('pet_name')
        diagnosis = request.POST.get('diagnosis')
        admission_date = request.POST.get('admission_date')

        # Tạo một hồ sơ nhập viện mới
        pet = PetHospitalization(pet_name=pet_name, diagnosis=diagnosis, admission_date=admission_date)
        pet.save()

        return redirect('pet')

    return render(request, 'Nhanvien/add_pet.html')


def room(request):
    cages = Booking.objects.filter(status='NHAP_VIEN')  # Chỉ lấy các thú cưng đang nhập viện
    return render(request, 'Nhanvien/room.html', {'cages': cages})


# Thêm mới phòng khám
def add_room(request):
    if request.method == 'POST':
        # Lấy thông tin từ form
        room_number = request.POST.get('room_number')
        capacity = request.POST.get('capacity')

        # Tạo một phòng khám mới
        room = Room(room_number=room_number, capacity=capacity)
        room.save()

        return redirect('room')

    return render(request, 'Nhanvien/add_room.html')

# Đăng nhập
def login(request):
    return render(request, 'home/login.html')
