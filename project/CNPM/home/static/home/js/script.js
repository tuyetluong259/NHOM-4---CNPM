function showForm(formId) {
    document.querySelectorAll('.auth-form').forEach(form => form.classList.remove('active'));
    document.querySelectorAll('.tab-button').forEach(tab => tab.classList.remove('active'));
    document.getElementById(formId).classList.add('active');
    event.target.classList.add('active');
}

function handleLogin() {
    const role = document.getElementById("loginRole").value;
    let redirectURL = "";

    switch (role) {
        case "admin":
            redirectURL = "/admin";
            break;
        case "nhanvien":
            redirectURL = "/Nhanvien";
            break;
        case "bacsi":
            redirectURL = "/doctor_dashboard";
            break;
        case "khachhang":
            redirectURL = "/customer_dashboard";
            break;
        default:
            alert("Vui lòng chọn vai trò hợp lệ!");
            return;
    }

    window.location.href = redirectURL;
}
