from django.shortcuts import render, redirect, get_object_or_404
from .models import Phong, ThuCung, Booking, LichKham

# Trang chủ
def index(request):
    context = {}
    return render(request, 'index.html', context)

# Quản lý phòng (chuồng)
def list_phong(request):
    rooms = Phong.objects.all()
    if request.method == 'POST':
        ten_phong = request.POST['ten_phong']
        loai_phong = request.POST['loai_phong']
        suc_chua = request.POST['suc_chua']
        Phong.objects.create(ten_phong=ten_phong, loai_phong=loai_phong, suc_chua=suc_chua)
        return redirect('list_phong')
    return render(request, 'rooms.html', {'rooms': rooms})

# Quản lý thú cưng
def list_thucung(request):
    pets = ThuCung.objects.select_related('phong').all()
    rooms = Phong.objects.all()
    if request.method == 'POST':
        pet_name = request.POST['pet_name']
        pet_type = request.POST['pet_type']
        phong_id = request.POST.get('phong')
        phong = get_object_or_404(Phong, id=phong_id)
        ThuCung.objects.create(ten=pet_name, loai=pet_type, phong=phong)
        return redirect('list_thucung')
    return render(request, 'pets.html', {'pets': pets, 'rooms': rooms})

# Quản lý booking
def list_booking(request):
    bookings = Booking.objects.all()  # Lấy tất cả booking
    return render(request, 'bookings.html', {'bookings': bookings})

# Hủy booking
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.trang_thai = 'Cancelled'
    booking.save()
    # Thêm logic hoàn tiền nếu cần
    return redirect('list_booking')

# Quản lý lịch khám bác sĩ thú y
def list_lichkham(request):
    schedules = LichKham.objects.all()
    if request.method == 'POST':
        ten_thu_cung = request.POST['ten_thu_cung']
        ten_bac_si = request.POST['ten_bac_si']
        thoi_gian = request.POST['thoi_gian']
        LichKham.objects.create(ten_thu_cung=ten_thu_cung, ten_bac_si=ten_bac_si, thoi_gian=thoi_gian)
        return redirect('list_lichkham')
    return render(request, 'schedule.html', {'schedules': schedules})
