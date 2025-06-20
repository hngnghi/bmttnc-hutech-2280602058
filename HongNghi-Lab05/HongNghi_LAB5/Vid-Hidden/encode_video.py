import cv2
import numpy as np
import os

def encode_message_in_video(input_path, output_path, secret_message):
    # Kiểm tra tệp đầu vào
    if not os.path.exists(input_path):
        print(f"❌ Tệp video không tồn tại: {input_path}")
        return False

    # Mở video đầu vào
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"❌ Không mở được video: {input_path}")
        print("Kiểm tra: Tệp có thể bị hỏng hoặc định dạng không được hỗ trợ.")
        return False

    # Lấy thông tin video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Tính số bit tối đa có thể nhúng
    max_bits = frame_count * width * height * 3  

    # Chuyển thông điệp thành chuỗi nhị phân + mã kết thúc
    secret_message += "####"
    binary_msg = ''.join(format(ord(c), '08b') for c in secret_message)
    msg_len = len(binary_msg)

    # Kiểm tra xem thông điệp có quá dài hay không
    if msg_len > max_bits:
        print(f"❌ Thông điệp quá dài ({msg_len} bit) so với dung lượng video ({max_bits} bit).")
        cap.release()
        return False

    # Khởi tạo video đầu ra
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    if not out.isOpened():
        print(f"❌ Không thể tạo video đầu ra: {output_path}")
        cap.release()
        return False

    msg_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_copy = frame.copy()
        for i in range(height):
            for j in range(width):
                pixel = frame_copy[i, j]
                for k in range(3):  # BGR
                    if msg_idx < msg_len:
                        # Lấy bit ít ý nghĩa nhất (LSB) và thay bằng bit từ thông điệp
                        bit = int(binary_msg[msg_idx])
                        # Giữ nguyên các bit khác và chỉ thay đổi LSB
                        pixel[k] = (pixel[k] & 0xFE) | bit  # 0xFE = 11111110 (giữ 7 bit cao, thay bit thấp)
                        msg_idx += 1
                frame_copy[i, j] = pixel

        out.write(frame_copy)

    if msg_idx < msg_len:
        print("⚠️ Cảnh báo: Video quá ngắn, thông điệp chưa được nhúng hết.")
        cap.release()
        out.release()
        return False

    cap.release()
    out.release()
    print(f"✅ Giấu tin hoàn tất vào {output_path}")
    return True

if __name__ == "__main__":
    input_video = r"D:\BMTT_NangCao\ThaiNguyen_Lap05\Vid-Hidden\Video.avi"  # Đường dẫn cố định
    output_video = r"D:\BMTT_NangCao\ThaiNguyen_Lap05\Vid-Hidden\encoded.avi"  # Đường dẫn đầu ra
    encode_message_in_video(input_video, output_video, "Hello world!")
