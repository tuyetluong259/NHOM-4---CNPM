document.addEventListener("DOMContentLoaded", function () {
  showForm("loginForm");

  document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault();
    handleLogin();
  });

  document.getElementById("registerForm").addEventListener("submit", function (event) {
    event.preventDefault();
    handleRegister();
  });
});

// Chuyển đổi giữa form đăng nhập và đăng ký
function showForm(formId) {
  document.querySelectorAll(".auth-form").forEach(form => form.classList.remove("active"));
  document.querySelectorAll(".tab-button").forEach(tab => tab.classList.remove("active"));

  const formToShow = document.getElementById(formId);
  if (formToShow) {
    formToShow.classList.add("active");
  } else {
    console.error("Không tìm thấy form: " + formId);
  }

  if (formId === "loginForm") {
    document.getElementById("loginTab").classList.add("active");
  } else if (formId === "registerForm") {
    document.getElementById("registerTab").classList.add("active");
  }
}

// Xử lý đăng nhập
async function handleLogin() {
  const email = document.getElementById("loginEmail").value.trim();
  const password = document.getElementById("loginPassword").value.trim();
  const role = document.getElementById("loginRole").value;
  const loginBtn = document.getElementById("loginSubmit");

  if (!email || !password) {
    return showAlert("Vui lòng nhập đầy đủ email và mật khẩu!", "error");
  }

  if (!isValidEmail(email)) {
    return showAlert("Vui lòng nhập email hợp lệ!", "error");
  }

  loginBtn.disabled = true;
  loginBtn.textContent = "Đang đăng nhập...";

  try {
    const response = await fetch("/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken(),
      },
      body: JSON.stringify({ email, password, role }),
    });

    const data = await response.json();
    if (data.success) {
      window.location.href = data.redirect_url;
    } else {
      showAlert(data.message || "Đăng nhập thất bại!", "error");
    }
  } catch (error) {
    console.error("Lỗi đăng nhập:", error);
    showAlert("Đã xảy ra lỗi, vui lòng thử lại!", "error");
  } finally {
    loginBtn.disabled = false;
    loginBtn.textContent = "Đăng nhập";
  }
}

// Xử lý đăng ký
async function handleRegister() {
  const email = document.getElementById("registerEmail").value.trim();
  const password = document.getElementById("registerPassword").value.trim();
  const confirmPassword = document.getElementById("registerConfirmPassword").value.trim();
  const registerBtn = document.getElementById("registerSubmit");

  if (!email || !password || !confirmPassword) {
    return showAlert("Vui lòng nhập đầy đủ thông tin!", "error");
  }

  if (password !== confirmPassword) {
    return showAlert("Mật khẩu nhập lại không khớp!", "error");
  }

  if (!isValidEmail(email)) {
    return showAlert("Vui lòng nhập email hợp lệ!", "error");
  }

  registerBtn.disabled = true;
  registerBtn.textContent = "Đang đăng ký...";

  try {
    const response = await fetch("/register/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken(),
      },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();
    if (data.success) {
      showAlert("Đăng ký thành công! Vui lòng đăng nhập.", "success");
      showForm("loginForm");
    } else {
      showAlert(data.message || "Đăng ký thất bại!", "error");
    }
  } catch (error) {
    console.error("Lỗi đăng ký:", error);
    showAlert("Đã xảy ra lỗi, vui lòng thử lại!", "error");
  } finally {
    registerBtn.disabled = false;
    registerBtn.textContent = "Đăng ký";
  }
}

// Kiểm tra định dạng email
function isValidEmail(email) {
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return emailRegex.test(email);
}

// Lấy CSRF token từ cookie hoặc input ẩn
function getCSRFToken() {
  const tokenInput = document.querySelector("input[name='csrfmiddlewaretoken']");
  if (tokenInput) return tokenInput.value;

  const cookie = document.cookie.split("; ").find(row => row.startsWith("csrftoken="));
  return cookie ? cookie.split("=")[1] : "";
}

// Hiển thị thông báo
function showAlert(message, type = "info") {
  const alertBox = document.getElementById("alertBox");
  if (!alertBox) return alert(message);

  alertBox.textContent = message;
  alertBox.className = `alert ${type}`;
  alertBox.style.display = "block";

  setTimeout(() => {
    alertBox.style.display = "none";
  }, 3000);
}
