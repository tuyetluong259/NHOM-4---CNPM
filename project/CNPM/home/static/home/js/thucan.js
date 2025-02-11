const btn = document.querySelectorAll(".add-to-cart") 
// console.log(btn)
btn.forEach(function(button,index){
    button.addEventListener("click", function(event){{
        var btnItem = event.target;
        var product = btnItem.closest(".card");
        var productImg = product.querySelector("img").src
        var productName = product.querySelector("h4").innerText
        var productPrice = product.querySelector(".product-price").innerText
        addcart(productPrice, productImg, productName)
    }})
})
function addcart(productPrice, productImg, productName) {
    var imgSrc = productImg.includes("http") ? productImg : "/static/" + productImg.replace("/static/", "");    
    var addtr = document.createElement("tr")
   var cartItem = document.querySelectorAll("tbody tr") 
   for (var i=0;i<cartItem.length;i++) {
        var productT = document.querySelectorAll(".title")
        if(productT[i].innerHTML == productName ) {

            alert("Sản phẩm của bạn đã có trong giỏ hàng!")
            return
        }
    }
    var trcontent = '<tr><td class="d-flex align-items-center justify-content-center"><img src="'+imgSrc+'" class="me-2" width="100"/> <span class="title">'+productName+'</span> </td><td><span class="price">'+productPrice+'</span> <sup>đ</sup></td> <td> <input type="number" value="1" min="1" class="form-control w-50 mx-auto"/></td> <td class="text-danger" style="cursor: pointer"><span class="delete">Xóa</span></td></tr>'
     addtr.innerHTML = trcontent
    var cartTable = document.querySelector("tbody")
    cartTable.append(addtr)

    carttotal()
    deleteCart();
}

function carttotal() {
    var cartItem = document.querySelectorAll("tbody tr");
    var totalC = 0;

    cartItem.forEach(function(row) {
        var inputValue = row.querySelector("input").value;
        var productPrice = row.querySelector(".price").innerHTML;
        totalC += inputValue * productPrice * 1000;
    });

    var cartTotalA = document.querySelector(".text-end span");
    cartTotalA.innerHTML = totalC > 0 ? totalC.toLocaleString('de-DE') : "0"; // Đảm bảo hiển thị 0 khi giỏ hàng rỗng
}

//delette
function deleteCart() {
    var deleteButtons = document.querySelectorAll(".delete");

    deleteButtons.forEach(function(button) {
        button.addEventListener("click", function(event) {
            var cartDelete = event.target;
            var cartItem = cartDelete.closest("tr"); // Tìm hàng chứa sản phẩm
            cartItem.remove(); // Xóa hàng

            carttotal(); // Cập nhật tổng tiền
        });
    });
}