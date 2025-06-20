import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import base64
from PIL import Image
import img_hidden.encrypt as steg_encrypt
import img_hidden.decrypt as steg_decrypt
from blockchain.blockchain import Blockchain
import ssl
import socket
import cv2

# ==== Hàm xử lý video steganography ====
def encode_pixel(pixel, bits):
    r, g, b = pixel
    r = (r & 0b11111110) | int(bits[0])
    g = (g & 0b11111110) | int(bits[1])
    b = (b & 0b11111110) | int(bits[2])
    return r, g, b

def encode_video(input_path, output_path, message):
    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    message += '###'
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
                    frame[y, x] = encode_pixel(frame[y, x], bits)
                    idx += 3
        out.write(frame)

    cap.release()
    out.release()

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

    chars = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    message = ''.join(chars)
    return message.split('###')[0]

# ==== Cấu hình giao diện chính ====
root = tk.Tk()
root.title("Tổng hợp Bài thực hành - UI Desktop")
root.geometry("800x600")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# ===============================
# TAB 1: MÃ HÓA / GIẢI MÃ BASE64
# ===============================
tab_base64 = ttk.Frame(notebook)
notebook.add(tab_base64, text="🔐 Base64")

entry_base64_input = tk.Text(tab_base64, height=5)
entry_base64_input.pack(pady=5)

entry_base64_output = tk.Text(tab_base64, height=5, bg="#f0f0f0")
entry_base64_output.pack(pady=5)

def do_base64_encode():
    raw = entry_base64_input.get("1.0", tk.END).strip()
    encoded = base64.b64encode(raw.encode()).decode()
    entry_base64_output.delete("1.0", tk.END)
    entry_base64_output.insert(tk.END, encoded)

def do_base64_decode():
    raw = entry_base64_input.get("1.0", tk.END).strip()
    try:
        decoded = base64.b64decode(raw.encode()).decode()
        entry_base64_output.delete("1.0", tk.END)
        entry_base64_output.insert(tk.END, decoded)
    except:
        messagebox.showerror("Lỗi", "Không giải mã được!")

tk.Button(tab_base64, text="Mã hóa", command=do_base64_encode).pack(pady=2)
tk.Button(tab_base64, text="Giải mã", command=do_base64_decode).pack(pady=2)

# =======================
# TAB 2: BLOCKCHAIN DEMO
# =======================
tab_chain = ttk.Frame(notebook)
notebook.add(tab_chain, text="⛓️ Blockchain")

blockchain = Blockchain()
blockchain.add_transaction("Alice", "Bob", 10)
proof = blockchain.proof_of_work(blockchain.get_previous_block().proof)
blockchain.create_block(proof, blockchain.get_previous_block().hash)

output_chain = tk.Text(tab_chain)
output_chain.pack(expand=True, fill='both')

for block in blockchain.chain:
    output_chain.insert(tk.END, f"🔢 Block {block.index}\n")
    output_chain.insert(tk.END, f"📦 Giao dịch: {block.transactions}\n")
    output_chain.insert(tk.END, f"🔗 Hash: {block.hash}\n")
    output_chain.insert(tk.END, "-----------------------------\n")

# ==============================
# TAB 3: GIẤU/HIỆN TIN TRONG ẢNH
# ==============================
tab_steg = ttk.Frame(notebook)
notebook.add(tab_steg, text="🖼️ Steganography")

img_path = tk.StringVar()
msg_to_hide = tk.StringVar()

def browse_image():
    path = filedialog.askopenfilename(filetypes=[("Image", "*.png *.jpg")])
    img_path.set(path)

def steg_encode():
    if not img_path.get() or not msg_to_hide.get():
        messagebox.showwarning("Thiếu", "Chọn ảnh và nhập thông điệp")
        return
    steg_encrypt.encode_image(img_path.get(), msg_to_hide.get())
    messagebox.showinfo("OK", "Đã mã hóa thành encoded_image.png")

def steg_decode():
    try:
        msg = steg_decrypt.decode_image("encoded_image.png")
        messagebox.showinfo("Giải mã", msg)
    except:
        messagebox.showerror("Lỗi", "Không giải mã được ảnh")

tk.Button(tab_steg, text="📂 Chọn ảnh", command=browse_image).pack()
tk.Entry(tab_steg, textvariable=img_path, width=60).pack()
tk.Label(tab_steg, text="📨 Thông điệp cần giấu:").pack()
tk.Entry(tab_steg, textvariable=msg_to_hide, width=60).pack()
tk.Button(tab_steg, text="💾 Mã hóa vào ảnh", command=steg_encode).pack(pady=2)
tk.Button(tab_steg, text="🔍 Giải mã từ ảnh", command=steg_decode).pack(pady=2)

# ===========================
# TAB 4: GỬI TIN SSL CLIENT
# ===========================
tab_ssl = ttk.Frame(notebook)
notebook.add(tab_ssl, text="🔒 SSL Client")

ssl_msg = tk.StringVar()
ssl_output = tk.Text(tab_ssl, height=10)

def send_ssl_message():
    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        with socket.create_connection(('localhost', 12345)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                ssock.send(ssl_msg.get().encode())
                data = ssock.recv(1024)
                ssl_output.insert(tk.END, "📩 Server trả về: " + data.decode() + "\n")
    except Exception as e:
        messagebox.showerror("Lỗi kết nối", str(e))

tk.Label(tab_ssl, text="💬 Nhập thông điệp gửi đến SSL Server:").pack()
tk.Entry(tab_ssl, textvariable=ssl_msg, width=60).pack()
tk.Button(tab_ssl, text="📤 Gửi", command=send_ssl_message).pack()
ssl_output.pack()

# === TAB Video Stego ===
tab_video = ttk.Frame(notebook)
notebook.add(tab_video, text="🎬 Video Stego")

video_path = tk.StringVar()
video_message = tk.StringVar()

def browse_video():
    path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4"), ("All", "*.*")])
    video_path.set(path)

def encode_video_ui():
    if not video_path.get() or not video_message.get():
        messagebox.showwarning("Thiếu", "Vui lòng chọn video và nhập thông điệp.")
        return
    output = video_path.get().replace(".mp4", "_encoded.avi")
    encode_video(video_path.get(), output, video_message.get())
    messagebox.showinfo("OK", f"Đã mã hóa vào {output}")

def decode_video_ui():
    path = filedialog.askopenfilename(filetypes=[("AVI files", "*.avi")])
    if not path:
        return
    msg = decode_video(path)
    messagebox.showinfo("Thông điệp", msg)

tk.Button(tab_video, text="Chọn video", command=browse_video).pack(pady=2)
tk.Entry(tab_video, textvariable=video_path, width=70).pack()
tk.Label(tab_video, text="Thông điệp muốn giấu:").pack()
tk.Entry(tab_video, textvariable=video_message, width=50).pack()
tk.Button(tab_video, text="Giấu tin vào video", command=encode_video_ui).pack(pady=5)
tk.Button(tab_video, text="Giải mã video", command=decode_video_ui).pack(pady=5)

# === Chạy ứng dụng ===
root.mainloop()
