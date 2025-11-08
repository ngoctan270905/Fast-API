# 🧩 RESTful API Status Codes & CRUD Mapping

## 🧩 1️⃣ Bảng trạng thái chuẩn RESTful API

| Nhóm | Mã | Tên (Status) | Khi nào dùng |
|------|----|---------------|---------------|
| ✅ **Thành công (Success)** | 200 | **OK** | Request thành công (GET, PUT, PATCH) |
|  | 201 | **Created** | Tạo mới thành công (POST) |
|  | 202 | **Accepted** | Request được chấp nhận nhưng xử lý sau (ví dụ: tác vụ nền) |
|  | 204 | **No Content** | Thành công nhưng không có dữ liệu trả về (thường dùng với DELETE hoặc PUT) |
| ⚠️ **Lỗi từ client (Client Errors)** | 400 | **Bad Request** | Request sai (thiếu tham số, format sai, validate lỗi) |
|  | 401 | **Unauthorized** | Chưa xác thực (chưa login hoặc token sai) |
|  | 403 | **Forbidden** | Đã login nhưng không có quyền truy cập |
|  | 404 | **Not Found** | Không tìm thấy tài nguyên (ID, URL, endpoint sai) |
|  | 405 | **Method Not Allowed** | Sử dụng sai method (VD: gọi `POST` vào `/users/{id}` thay vì `GET`) |
|  | 409 | **Conflict** | Xung đột dữ liệu (VD: tạo user đã tồn tại, duplicate email) |
|  | 422 | **Unprocessable Entity** | Dữ liệu hợp lệ về cú pháp nhưng sai về nội dung (VD: sai kiểu dữ liệu, FastAPI dùng cho lỗi validate Pydantic) |
| 💥 **Lỗi từ server (Server Errors)** | 500 | **Internal Server Error** | Lỗi nội bộ backend (bug, exception chưa xử lý) |
|  | 502 | **Bad Gateway** | Server trung gian (proxy) lỗi |
|  | 503 | **Service Unavailable** | Dịch vụ tạm ngưng (bảo trì, downtime) |
|  | 504 | **Gateway Timeout** | Quá thời gian chờ phản hồi từ server khác |

---

## 🧠 2️⃣ CRUD Mapping chuẩn RESTful

| Hành động | HTTP Method | Mã trạng thái chính | Mô tả |
|------------|--------------|----------------------|--------|
| 🔍 **Read all** | `GET /users` | `200 OK` | Trả về danh sách tài nguyên |
| 🔍 **Read one** | `GET /users/{id}` | `200 OK / 404 Not Found` | Trả về 1 tài nguyên hoặc báo không tồn tại |
| ➕ **Create** | `POST /users` | `201 Created` | Tạo mới thành công, có thể trả về object hoặc location |
| ✏️ **Update (replace)** | `PUT /users/{id}` | `200 OK / 204 No Content` | Cập nhật toàn bộ object |
| 🧩 **Partial update** | `PATCH /users/{id}` | `200 OK / 204 No Content` | Cập nhật 1 phần dữ liệu |
| 🗑️ **Delete** | `DELETE /users/{id}` | `204 No Content` | Xóa tài nguyên thành công |
| ❌ **Delete fail** | `DELETE /users/{id}` | `404 Not Found` | Không tìm thấy tài nguyên để xóa |
