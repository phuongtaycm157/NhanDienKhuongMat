import os
import cv2

from randomString import randomString
from DB import UserRegisterImagesCollection as URIC
from FaceRecognition import faceRecognition

# Khởi tạo người dùng
user = {"username": "", "images": []}

# Xác nhận tên người chụp ảnh
print('Tên của bạn là: ')
username = input()

# lưu tên người dùng và tạo token
user['username'] = username
token = randomString(10)

# Đường đẫn của ảnh.
dir = './images/'+username+'/'

# Tạo thư mục chứa ảnh.
os.mkdir('.\\images\\'+username)

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
        if takeAPhoto:
            count += 1
            photoName = dir + token + '_' + str(count) + '.png'
            # Lưu dường đẫn hình vào database.
            user['images'].append(photoName)
            # Lưu hình vào thư mục image
            cv2.imwrite(photoName, frame)
            takeAPhoto = False
        frame = faceRecognition(frame, 1.2, 5)
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

if user["images"]:
    URIC.insert_one(user)
else:
    os.rmdir('.\\images\\'+username)

# Đóng hết các cửa sổ
cv2.destroyAllWindows()