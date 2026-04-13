import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("[+] Generating keys...")
os.system("python keygen.py")

print("[+] Signing file...")
os.system("python sign.py")

print("[+] Verifying (original file)...")
os.system("python verify.py")

print("[+] Modifying file...")
with open("data/file.txt", "a") as f:
    f.write("\nThis line was added (tampered).")
