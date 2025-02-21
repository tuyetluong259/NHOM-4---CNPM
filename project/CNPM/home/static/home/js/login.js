// Lấy các phần tử cần thiết
const loginFormContainer = document.getElementById('login-form');
const registerFormContainer = document.getElementById('register-form');
const showRegisterLink = document.getElementById('showRegister');
const showLoginLink = document.getElementById('showLogin');

// Chuyển đổi form
showRegisterLink.addEventListener('click', () => {
  loginFormContainer.classList.remove('active');
  registerFormContainer.classList.add('active');
});

showLoginLink.addEventListener('click', () => {
  registerFormContainer.classList.remove('active');
  loginFormContainer.classList.add('active');
});

// Xử lý sự kiện submit form đăng nhập
document.getElementById('loginForm').addEventListener('submit', function(e) {
  e.preventDefault();
  // Lấy dữ liệu từ form đăng nhập
  const email = document.getElementById('loginEmail').value;
  const password = document.getElementById('loginPassword').value;
  // Xử lý đăng nhập (demo: in ra console)
  console.log("Đăng nhập với:", { email, password });
  alert("Đăng nhập thành công!");
  // Bạn có thể chuyển trang hoặc lưu thông tin đăng nhập ở đây
});

// Xử lý sự kiện submit form đăng ký
document.getElementById('registerForm').addEventListener('submit', function(e) {
  e.preventDefault();
  // Lấy dữ liệu từ form đăng ký
  const name = document.getElementById('regName').value;
  const email = document.getElementById('regEmail').value;
  const password = document.getElementById('regPassword').value;
  // Xử lý đăng ký (demo: in ra console)
  console.log("Đăng ký với:", { name, email, password });
  alert("Đăng ký thành công!");
  // Bạn có thể chuyển sang trang đăng nhập hoặc tự động đăng nhập sau khi đăng ký
});
