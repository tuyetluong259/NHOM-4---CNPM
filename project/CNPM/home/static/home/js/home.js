window.onscroll = function() {myFunction()};

var header = document.getElementById("myHeader");
var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}
// Open the full screen search box
function openSearch() {
    document.getElementById("myOverlay").style.display = "block";
  }
  
  // Close the full screen search box
  function closeSearch() {
    document.getElementById("myOverlay").style.display = "none";
  }
  function myAccFunc() {
    var x = document.getElementById("demoAcc");
    if (x.className.indexOf("w3-show") == -1) {
      x.className += " w3-show";
      x.previousElementSibling.className += " w3-green";
    } else { 
      x.className = x.className.replace(" w3-show", "");
      x.previousElementSibling.className = 
      x.previousElementSibling.className.replace(" w3-green", "");
    }
  }
  
  function myDropFunc() {
    var x = document.getElementById("demoDrop");
    if (x.className.indexOf("w3-show") == -1) {
      x.className += " w3-show";
      x.previousElementSibling.className += " w3-green";
    } else { 
      x.className = x.className.replace(" w3-show", "");
      x.previousElementSibling.className = 
      x.previousElementSibling.className.replace(" w3-green", "");
    }
  }
  document.addEventListener("DOMContentLoaded", function () {
    const cart = []; // Mảng chứa sản phẩm trong giỏ hàng
    const btns = document.querySelectorAll(".add-to-cart");

    btns.forEach((btn) => {
        btn.addEventListener("click", function (event) {
            event.preventDefault(); // Ngăn chặn load lại trang khi bấm vào <a>

            // Lấy thông tin sản phẩm từ data-attributes
            const productId = btn.getAttribute("data-id");
            const productName = btn.getAttribute("data-name");
            const productPrice = btn.getAttribute("data-price");

            // Tạo object sản phẩm
            const product = {
                id: productId,
                name: productName,
                price: productPrice,
                quantity: 1
            };

            // Kiểm tra xem sản phẩm đã có trong giỏ chưa
            const index = cart.findIndex((item) => item.id === productId);
            if (index !== -1) {
                cart[index].quantity += 1;
            } else {
                cart.push(product);
            }

            // Cập nhật giỏ hàng trên giao diện
            updateCartUI();
        });
    });

    // Hàm cập nhật giỏ hàng trên giao diện
    function updateCartUI() {
        const cartContainer = document.getElementById("cart-items");
        cartContainer.innerHTML = ""; // Xóa danh sách cũ

        cart.forEach((item) => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${item.name}</td>
                <td>${item.price} đ</td>
                <td>${item.quantity}</td>
                <td><button class="remove-item" data-id="${item.id}">Xóa</button></td>
            `;
            cartContainer.appendChild(row);
        });

        // Xử lý sự kiện xóa sản phẩm
        document.querySelectorAll(".remove-item").forEach((btn) => {
            btn.addEventListener("click", function () {
                const productId = btn.getAttribute("data-id");
                const index = cart.findIndex((item) => item.id === productId);
                if (index !== -1) {
                    cart.splice(index, 1); // Xóa sản phẩm khỏi giỏ
                    updateCartUI();
                }
            });
        });
    }
});
