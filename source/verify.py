from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
import os, base64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sig_path = os.path.join(BASE_DIR, "signature/sig.bin")

print("===== HE THONG XAC MINH CHU KY SO =====")


text = input("Nhap noi dung can xac minh: ")

if not os.path.exists(sig_path):
    print("\n[!] Khong tim thay file chu ky: signature/sig.bin")
    print("    Hay chay sign.py truoc de tao chu ky.")
    exit(1)

with open(sig_path, "rb") as f:
    signature = f.read()


pub_key_path = os.path.join(BASE_DIR, "keys/public.pem")

if not os.path.exists(pub_key_path):
    print("\n[!] Khong tim thay public key: keys/public.pem")
    print("    Hay chay keygen.py truoc de tao cap khoa.")
    exit(1)

with open(pub_key_path, "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

data = text.encode()

sig_base64 = base64.b64encode(signature).decode()

print("\n===== KET QUA XAC MINH =====")
print("Noi dung kiem tra:")
print("   >", text)

print("\nChu ky (base64):")
print(sig_base64)

try:
    public_key.verify(
        signature,
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("\n[OK] CHU KY HOP LE")
    print("     Noi dung nay chinh xac va khong bi chinh sua.")

except InvalidSignature:
    print("\n[FAIL] CHU KY KHONG HOP LE")
    print("       Noi dung da bi chinh sua hoac chu ky sai.")