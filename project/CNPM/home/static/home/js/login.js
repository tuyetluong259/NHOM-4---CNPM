document.addEventListener("DOMContentLoaded", function () {
  // Mặc định hiển thị form đăng nhập
  showForm("loginForm");

  // Gán sự kiện cho form đăng nhập
  document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault();
    handleLogin();
  });

  // Gán sự kiện cho form đăng ký
  document.getElementById("registerForm").addEventListener("submit", function (event) {
    event.preventDefault();
    handleRegister();
  });
});

// Chuyển đổi giữa đăng nhập và đăng ký
function showForm(formId) {
  document.querySelectorAll(".auth-form").forEach(form => form.classList.remove("active"));
  document.querySelectorAll(".tab-button").forEach(tab => tab.classList.remove("active"));

  document.getElementById(formId).classList.add("active");
  
  // Tìm tab-button phù hợp và thêm class "active"
  document.querySelector(`[onclick="showForm('${formId}')"]`).classList.add("active");
}

// Xử lý đăng nhập
function handleLogin() {
  const role = document.getElementById("loginRole").value;
  const email = document.getElementById("loginEmail").value.trim();
  const password = document.getElementById("loginPassword").value.trim();

  if (!email || !password) {
    alert("Vui lòng nhập đầy đủ thông tin!");
    return;
  }

  // Đảm bảo email hợp lệ (regex)
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  if (!emailRegex.test(email)) {
    alert("Vui lòng nhập địa chỉ email hợp lệ!");
    return;
  }

  fetch("/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRFToken()
    },
    body: JSON.stringify({ role, email, password })
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      window.location.href = data.redirect_url;
    } else {
      alert(data.message || "Đăng nhập thất bại! Kiểm tra lại tài khoản.");
    }
  })
  .catch(error => {
    console.error("Lỗi:", error);
    alert("Đã xảy ra lỗi. Vui lòng thử lại sau!");
  });
}

// Xử lý đăng ký
function handleRegister() {
  const email = document.getElementById("registerEmail").value.trim();
  const password = document.getElementById("registerPassword").value.trim();
  const confirmPassword = document.getElementById("registerConfirmPassword").value.trim();

  if (!email || !password || !confirmPassword) {
    alert("Vui lòng nhập đầy đủ thông tin!");
    return;
  }

  if (password !== confirmPassword) {
    alert("Mật khẩu nhập lại không khớp!");
    return;
  }

  // Đảm bảo email hợp lệ (regex)
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  if (!emailRegex.test(email)) {
    alert("Vui lòng nhập địa chỉ email hợp lệ!");
    return;
  }

  fetch("/register/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRFToken()
    },
    body: JSON.stringify({ email, password })
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      alert("Đăng ký thành công! Vui lòng đăng nhập.");
      showForm("loginForm");
    } else {
      alert(data.message || "Đăng ký thất bại! Vui lòng thử lại.");
    }
  })
  .catch(error => {
    console.error("Lỗi:", error);
    alert("Đã xảy ra lỗi. Vui lòng thử lại sau!");
  });
}

// Lấy CSRF token từ cookie hoặc thẻ hidden
function getCSRFToken() {
  const tokenInput = document.querySelector("input[name='csrfmiddlewaretoken']");
  if (tokenInput) {
    return tokenInput.value;
  }
  const cookie = document.cookie.split("; ").find(row => row.startsWith("csrftoken="));
  return cookie ? cookie.split("=")[1] : "";
}
