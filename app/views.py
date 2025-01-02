from django.shortcuts import render
from django.http import HttpResponse
from .models import MedicalRecord

# Trang chủ
def home(request):
    context = {}
    return render(request, 'app/home.html', context)

# Ghi nhận hồ sơ khám bệnh
def record_medical(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        name = request.POST.get('name')
        species = request.POST.get('species')
        progress = request.POST.get('progress')

        # Lưu thông tin vào cơ sở dữ liệu
        medical_record = MedicalRecord(name=name, species=species, progress=progress)
        medical_record.save()

        # Gửi thông báo thành công
        context = {
            'success_message': 'Hồ sơ khám bệnh đã được ghi nhận!',
            'name': name,
            'species': species,
            'progress': progress
        }
    else:
        context = {}
    
    return render(request, 'app/record_medical.html', context)

# Chăm sóc thú cưng (hiển thị danh sách thú cưng nhập viện)
def inpatient_care(request):
    # Lấy danh sách hồ sơ từ cơ sở dữ liệu
    pets_in_hospital = MedicalRecord.objects.all()
    context = {'pets': pets_in_hospital}
    return render(request, 'app/inpatient_care.html', context)
