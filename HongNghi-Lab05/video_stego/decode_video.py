import cv2
import sys

def decode_video(path):
    cap = cv2.VideoCapture(path)
    binary = ''

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        for row in frame:
            for pixel in row:
                for channel in pixel[:3]:
                    binary += str(channel & 1)

    cap.release()

    print("📦 Độ dài chuỗi binary thu được:", len(binary))

    chars = []
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) < 8:
            break
        char = chr(int(byte, 2))
        if '###' in ''.join(chars) + char:
            break
        chars.append(char)

    message = ''.join(chars)
    print("📨 Chuỗi thô lấy được:", message)
    return message

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Cách dùng: python decode_video.py <video_encoded.avi>")
    else:
        path = sys.argv[1]
        msg = decode_video(path)
        print("✅ Thông điệp giải mã được:")
        print(msg)
