# Qu?n ly Chuồng
class QuanLyChuong:
    def __init__(self):
        self.phong = ["Phong A", "Phong B", "Phong C"]  # Danh sách các chuồng/phòng hiện có

    def hien_thi_phong(self):
        """Hiển thị danh sách các chuồng (phòng) hiện có trong hệ thống."""
        print("\nDanh sách các chuồng (phòng):")
        for index, room in enumerate(self.phong, start=1):
            print(f"{index}. {room}")

    def them_phong(self):
        """Thêm chuồng (phòng) mới vào hệ thống."""
        room_name = input("Nhập tên chuồng (phòng) mới: ")
        if room_name not in self.phong:
            self.phong.append(room_name)
            print(f"Chuồng (phòng) {room_name} đã được thêm vào hệ thống.")
        else:
            print("Chuồng (phòng) này đã tồn tại!")

    def xoa_phong(self):
        """Xóa một chuồng (phòng) trong hệ thống."""
        self.hien_thi_phong()
        try:
            room_id = int(input("Nhập số thứ tự chuồng (phòng) muốn xóa: "))
            if 1 <= room_id <= len(self.phong):
                removed_room = self.phong.pop(room_id - 1)
                print(f"Chuồng (phòng) {removed_room} đã bị xóa khỏi hệ thống.")
            else:
                print("Số thứ tự không hợp lệ!")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
        
    def sua_phong(self):
        """Sửa tên của một chuồng (phòng) trong hệ thống."""
        self.hien_thi_phong()
        try:
            room_id = int(input("Nhập số thứ tự chuồng (phòng) muốn sửa: "))
            if 1 <= room_id <= len(self.phong):
                new_name = input("Nhập tên mới cho chuồng (phòng): ")
                self.phong[room_id - 1] = new_name
                print(f"Chuồng (phòng) đã được đổi tên thành {new_name}.")
            else:
                print("Số thứ tự không hợp lệ!")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

# Ví dụ sử dụng trong chương trình
if __name__ == "__main__":
    quan_ly = QuanLyChuong()
    
    while True:
        print("\n--- Menu Quản lý Chuồng (Phòng) ---")
        print("1. Hiển thị danh sách chuồng (phòng)")
        print("2. Thêm chuồng (phòng) mới")
        print("3. Xóa chuồng (phòng)")
        print("4. Sửa tên chuồng (phòng)")
        print("5. Thoát")
        
        choice = input("Chọn chức năng (1-5): ")
        
        if choice == "1":
            quan_ly.hien_thi_phong()
        elif choice == "2":
            quan_ly.them_phong()
        elif choice == "3":
            quan_ly.xoa_phong()
        elif choice == "4":
            quan_ly.sua_phong()
        elif choice == "5":
            print("Thoát khỏi hệ thống.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
