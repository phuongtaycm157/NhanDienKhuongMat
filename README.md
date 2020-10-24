# Module Nhận Diện Khuôn Mặt

*** Những Phần hoàng thành ***

### Module nhận chụp ảnh
Đóng vai trò là phần register user's face

##### Tiền sử lý

Cài đặt các thư viện cần thiết: 
* `pip install opencv-python`
* `pip install pymongo`
* `pip install dnspython`

##### Kích hoạt hệ thống

`python main.py`

* Nhập tên người dụng trên terminal
* chọn cửa sổ mới xuất hiện *(vì chưa setup cửa sổ open on top)*
* Nhấn phím 't' để chụp
* nhấn phím 'q' thoát cửa sổ

##### Sử dụng Database để truy xuất dữ liệu

File DB.py đã setup đầy đủ kết nối với database DataMining

Database sử dụng là MongoDB

Đã tạo một collection trước đó là 'UserRegisterImagesCollection' và muốn sử dụng nó chỉ cần khai báo

```from DB import UserRegisterImagesCollection as URIC```

Copyright @Nishi
