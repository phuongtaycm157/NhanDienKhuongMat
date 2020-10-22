import cv2
from randomString import randomString
from DB import UserRegisterImagesCollection as URIC

# Khởi tạo người dùng
user = {"username": "", "images": []}

# Xác nhận tên người chụp ảnh
print('Tên của bạn là: ')
username = input()
# lưu tên người dùng
user['username'] = username
username += '_'+randomString(10)

# Đường đẫn của ảnh
dir = './images/'

# Id của webcam
camera_id = 0

# Mở camera
video = cv2.VideoCapture(camera_id)

# Cờ trạng thái của việc Chụp lại ảnh.
takeAPhoto = False
count = 0

while True:
    ret, frame = video.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if takeAPhoto:
            count += 1
            photoName = dir + username + '_' + str(count) + '.png'
            # Lưu dường đẫn hình vào database.
            user['images'].append(photoName)
            # Lưu hình vào thư mục image
            cv2.imwrite(photoName, frame)
            takeAPhoto = False
        cv2.imshow('Webcame', frame)

    key = cv2.waitKey(1)
    # Nhấn 'q' để thoát vòng lặp
    if key == ord('q'):
        break
    # Nhấn 't' để chụp lại một bức ảnh
    elif key == ord('t'):
        takeAPhoto = True

# Giải phóng camera
video.release()

URIC.insert_one(user)

# Đóng hết các cửa sổ
cv2.destroyAllWindows()