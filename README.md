# ung-dung-chu-ky-so-trong-quy-trinh-phe-duyet-van-ban-noi-bo
# ung-dung-chu-ky-so-trong-quy-trinh-phe-duyet-van-ban-noi-bo
# HỆ THỐNG CHỮ KÝ SỐ RSA

## 1. Giới thiệu

Chương trình mô phỏng hệ thống chữ ký số sử dụng thuật toán RSA kết hợp với hàm băm SHA-256.
Hệ thống cho phép:

* Sinh cặp khóa (Public Key / Private Key)
* Ký số dữ liệu
* Xác minh chữ ký số
* Kiểm tra tính toàn vẹn của dữ liệu
## 2. Cấu trúc chương trình

* `keygen.py` : Sinh cặp khóa RSA
* `sign.py` : Ký số dữ liệu
* `verify.py` : Xác minh chữ ký
* `main.py` : Chạy demo toàn bộ hệ thống

Thư mục:

* `keys/` : Lưu khóa công khai và bí mật
* `data/` : Lưu dữ liệu cần ký
* `signature/` : Lưu chữ ký
* 
## 3. Yêu cầu hệ thống

* Python 3.x
Cài đặt thư viện:

```bash
pip install cryptography
```

## 4. Cách chạy chương trình

Chạy file chính:

```bash
python main.py

## 5. Quy trình hoạt động

Chương trình thực hiện các bước:

1. Sinh cặp khóa RSA
2. Nhập nội dung và lưu vào file
3. Ký số dữ liệu bằng Private Key
4. Xác minh chữ ký bằng Public Key
5. Thay đổi dữ liệu và xác minh lại

## 6. Kết quả mong đợi

* Khi dữ liệu chưa bị thay đổi → chữ ký hợp lệ (VALID)
* Khi dữ liệu bị thay đổi → chữ ký không hợp lệ (INVALID)

## 7. Thuật toán sử dụng

* Thuật toán: RSA
* Hàm băm: SHA-256
* Cơ chế ký: PKCS#1 v1.5 hoặc PSS

## 8. Ý nghĩa

Hệ thống chứng minh:

* Tính toàn vẹn dữ liệu
* Tính xác thực nguồn gốc
* Phát hiện dữ liệu bị thay đổi

## 9. Lưu ý

* Không chỉnh sửa file sau khi ký nếu muốn verify thành công
* Nếu thay đổi dữ liệu, chữ ký sẽ không còn hợp lệ

## 10. Kết luận

Chương trình minh họa thành công cơ chế chữ ký số trong thực tế, giúp hiểu rõ nguyên lý hoạt động của RSA trong bảo mật thông tin.
