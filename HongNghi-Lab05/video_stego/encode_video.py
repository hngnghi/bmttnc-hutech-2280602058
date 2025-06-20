import cv2
import sys

def encode_pixel(pixel, bits):
    r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
    r = (r & 0b11111110) | int(bits[0])
    g = (g & 0b11111110) | int(bits[1])
    b = (b & 0b11111110) | int(bits[2])
    return [r, g, b]

def encode_video(input_path, output_path, message):
    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # ✅ dùng MJPG (ít nén)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    message += '###'  # dấu kết thúc
    binary = ''.join(format(ord(c), '08b') for c in message)
    idx = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        for y in range(height):
            for x in range(width):
                if idx + 3 <= len(binary):
                    bits = binary[idx:idx+3]
                    encoded = encode_pixel(frame[y, x], bits)
                    frame[y, x] = encoded
                    idx += 3
        out.write(frame)

    cap.release()
    out.release()
    print("✅ Đã tạo:", output_path)
    print("📤 Đã chèn", idx, "bit. 10 bit đầu:", binary[:10])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("❌ Cách dùng: python encode_video.py <video.mp4> <message>")
    else:
        input_path = sys.argv[1]
        message = sys.argv[2]
        output_path = input_path.replace(".mp4", "_encoded.avi")
        encode_video(input_path, output_path, message)
