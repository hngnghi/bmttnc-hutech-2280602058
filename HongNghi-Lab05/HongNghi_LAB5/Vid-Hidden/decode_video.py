import cv2
import os

def decode_message_from_video(video_path):
    # Kiểm tra tệp đầu vào
    if not os.path.exists(video_path):
        print(f"❌ Tệp video không tồn tại: {video_path}")
        return None

    # Mở video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"❌ Không mở được video: {video_path}")
        print("Kiểm tra: Tệp có thể bị hỏng hoặc định dạng không được hỗ trợ.")
        return None

    binary_data = ""
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        height, width, _ = frame.shape
        for i in range(height):
            for j in range(width):
                pixel = frame[i, j]
                for k in range(3):  # BGR
                    binary_data += str(pixel[k] & 1)

    cap.release()

    # Kiểm tra xem có đủ dữ liệu để giải mã không
    if len(binary_data) < 8:
        print("❌ Video quá ngắn, không đủ dữ liệu để giải mã.")
        return None

    # Tách từng byte (8 bit) và giải mã
    decoded = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) < 8:
            print("⚠️ Dữ liệu không đủ để tạo thành byte cuối cùng.")
            break
        try:
            char = chr(int(byte, 2))
            decoded += char
            if decoded.endswith("####"):
                print("🔍 Tin giấu được giải mã:")
                print(decoded[:-4])
                return decoded[:-4]
        except ValueError:
            print("⚠️ Lỗi giải mã: Gặp ký tự không hợp lệ.")
            return None

    print("❌ Không tìm thấy chuỗi kết thúc '####'.")
    return None

if __name__ == "__main__":
    decode_message_from_video(r"D:\BMTT_NangCao\ThaiNguyen_Lap05\Vid-Hidden\encoded.avi")