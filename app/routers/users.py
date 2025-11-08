# import class API từ thư viện API
from fastapi import APIRouter

# Định nghĩa route users
router = APIRouter(
    prefix="/users",  # dường dẫn gốc của API
    tags=["Users"],  # tên hiển thị cho nhóm API
)

# route enpoin con
@router.get("/")  # method : GET: users/
def get_users():
    return [
        {
            "id": 1,
            "username": 'Nguyễn Tấn'
        }
    ]

# route enpoin
@router.get("/{user_id}") # GET/ users/{user_id}
def get_user(user_id: int):
    return [
        {
            "id": {user_id},
            "name": f"User: {user_id}"
        }
    ]
