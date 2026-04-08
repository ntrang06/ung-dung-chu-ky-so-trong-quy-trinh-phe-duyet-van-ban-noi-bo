from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
import os, base64
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

data_path = os.path.join(BASE_DIR, "data/file.txt")
sig_path = os.path.join(BASE_DIR, "signature/sig.bin")

os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "signature"), exist_ok=True)

print("===== HE THONG KY SO =====")

# ===== 1. NHẬP =====
text = input("Nhap noi dung can ky: ")

# ===== 2. LƯU KHÔNG GHI ĐÈ =====
time_now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

with open(data_path, "a", encoding="utf-8") as f:
    f.write(f"[{time_now}] {text}\n")

print("[+] Da luu vao data/file.txt (khong ghi de)")

# ===== 3. KÝ CHỈ NỘI DUNG VỪA NHẬP =====
data = text.encode()

# ===== 4. LOAD PRIVATE KEY =====
with open(os.path.join(BASE_DIR, "keys/private.pem"), "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# ===== 5. KÝ =====
signature = private_key.sign(
    data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# ===== 6. LƯU CHỮ KÝ =====
with open(sig_path, "wb") as f:
    f.write(signature)

# ===== 7. HIỂN THỊ =====
sig_base64 = base64.b64encode(signature).decode()

print("\n===== KET QUA =====")
print("Da ky thanh cong")

print("\nNoi dung vua ky:")
print("   >", text)

print("\nChu ky (base64):")
print(sig_base64)

print("\nFile da luu:")
print("   data/file.txt")
print("   signature/sig.bin")