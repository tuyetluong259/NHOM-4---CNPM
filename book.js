// Constants for package services
const packageServices = {
    silver: [
        "Nhổ lông – Vệ sinh tai 🐾",
        "Tắm vệ sinh (vắt tuyến hôi) 🐾",
        "Sấy chải bông lông 🐾",
        "Chải lông chết 🐾",
        "Xịt nước hoa 🐾",
    ],
    gold: [
        "Nhổ lông – Vệ sinh tai 🐾",
        "Tắm vệ sinh (vắt tuyến hôi) 🐾",
        "Sấy chải bông lông 🐾",
        "Chải lông chết 🐾",
        "Xịt nước hoa 🐾",
        "Xịt dưỡng lông 🐾",
        "Cạo chân – Bụng – Hậu môn 🐾",
        "Cắt móng mài móng 🐾"
    ],
    platinum: [
        "Nhổ lông – Vệ sinh tai 🐾",
        "Tắm vệ sinh (vắt tuyến hôi) 🐾",
        "Sấy chải bông lông 🐾",
        "Chải lông chết 🐾",
        "Xịt nước hoa 🐾",
        "Xịt dưỡng lông 🐾",
        "Cạo chân – Bụng – Hậu môn 🐾",
        "Cắt móng mài móng 🐾",
        "Cạo lông toàn thân 🐾",
    ],
    diamond: [
        "Nhổ lông – Vệ sinh tai 🐾",
        "Tắm vệ sinh (vắt tuyến hôi) 🐾",
        "Sấy chải bông lông 🐾",
        "Chải lông chết 🐾",
        "Xịt nước hoa 🐾",
        "Xịt dưỡng lông 🐾",
        "Cạo chân – Bụng – Hậu môn 🐾",
        "Cắt móng mài móng 🐾",
        "Cắt tỉa tạo kiểu 🐾"
    ]
};

const dogWeights = [
    "0 - 2 kg", "2 - 4 kg", "4 - 7 kg", "7 - 10 kg", 
    "10 - 15 kg", "15 - 20 kg", "Trên 20 kg", "Trên 30 kg"
];

const catWeights = [
    "0 - 2 kg", "2 - 4 kg", "4 - 7 kg", "7 - 10 kg", "Trên 10 kg"
];

// Handle pet type selection
document.querySelectorAll('input[name="petType"]').forEach(radio => {
    radio.addEventListener('change', (e) => {
        const weightOptions = document.getElementById('weightOptions');
        weightOptions.style.display = 'block';
        weightOptions.innerHTML = '';
        const weights = e.target.value === 'dog' ? dogWeights : catWeights;
        weights.forEach(weight => {
            const label = document.createElement('label');
            label.innerHTML = `
                <input type="checkbox" name="weight" value="${weight}">
                ${weight}
            `;
            weightOptions.appendChild(label);
        });
    });
});

// Handle service selection
document.querySelectorAll('input[name="service"]').forEach(radio => {
    radio.addEventListener('change', (e) => {
        const packageDetails = document.getElementById('packageDetails');
        const selectedPackage = e.target.value;
        
        if (packageServices[selectedPackage]) {
            packageDetails.style.display = 'block';
            packageDetails.innerHTML = `
                <h3>QUY TRÌNH - ${selectedPackage.toUpperCase()}</h3>
                <ul>
                    ${packageServices[selectedPackage].map(service => `<li>${service}</li>`).join('')}
                </ul>
            `;
        }
    });
});

// Handle form submission
document.getElementById('serviceForm').addEventListener('submit', (e) => {
    e.preventDefault();
    // Add form submission logic here
});
// Add this to script.js
const nextButton = document.getElementById('nextButton');
const timeSection = document.getElementById('timeSection');
const daySelect = document.getElementById('daySelect');
const monthSelect = document.getElementById('monthSelect');
const yearSelect = document.getElementById('yearSelect');

// Populate day, month, year options
function populateDateSelectors() {
    for (let i = 1; i <= 31; i++) {
        daySelect.innerHTML += `<option value="${i}">${i}</option>`;
    }
    for (let i = 1; i <= 12; i++) {
        monthSelect.innerHTML += `<option value="${i}">${i}</option>`;
    }
    const currentYear = new Date().getFullYear();
    for (let i = currentYear; i <= currentYear + 5; i++) {
        yearSelect.innerHTML += `<option value="${i}">${i}</option>`;
    }
}

// Show the time section when "Tiếp Theo" is clicked
nextButton.addEventListener('click', () => {
    timeSection.classList.remove('hidden');
    populateDateSelectors();
});

const mainSelection = document.getElementById('mainSelection');
const registerSection = document.getElementById('registerSection');
const cancelSection = document.getElementById('cancelSection');
const registerButton = document.getElementById('registerService');
const cancelButton = document.getElementById('cancelService');

// Hiển thị giao diện Đăng Ký Dịch Vụ
registerButton.addEventListener('click', () => {
    mainSelection.classList.add('hidden');
    registerSection.classList.remove('hidden');
});

// Hiển thị giao diện Hủy Lịch Đăng Ký
cancelButton.addEventListener('click', () => {
    mainSelection.classList.add('hidden');
    cancelSection.classList.remove('hidden');
});

// Xử lý hủy lịch
document.getElementById('cancelForm').addEventListener('submit', (e) => {
    e.preventDefault();

    const appointmentId = document.getElementById('appointmentId').value;
    const originalDate = new Date(document.getElementById('originalDate').value);
    const today = new Date();

    if (!appointmentId || isNaN(originalDate.getTime())) {
        alert('Vui lòng nhập đầy đủ thông tin!');
        return;
    }

    const timeDiff = Math.ceil((originalDate - today) / (1000 * 60 * 60 * 24)); // Số ngày từ hôm nay đến ngày hẹn

    let refundMessage = '';

    if (timeDiff >= 7) {
        refundMessage = 'Bạn sẽ được hoàn 100% phí đã thanh toán.';
    } else if (timeDiff >= 3) {
        refundMessage = 'Bạn sẽ được hoàn 75% phí đã thanh toán.';
    } else if (timeDiff > 0) {
        refundMessage = 'Bạn sẽ không được hoàn phí đã thanh toán.';
    } else {
        refundMessage = 'Không thể hủy lịch hẹn vì đã qua ngày hẹn.';
    }

    alert(`Lịch hẹn với mã "${appointmentId}" đã được xử lý. ${refundMessage}`);
    mainSelection.classList.remove('hidden');
    cancelSection.classList.add('hidden');
});
// Show the time section when "Tiếp Theo" is clicked
nextButton.addEventListener('click', () => {
    timeSection.classList.remove('hidden');
    populateDateSelectors();
});
