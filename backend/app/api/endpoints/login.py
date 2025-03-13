from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserLogin, LoginResponse
from app.db.session import get_db_session
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=LoginResponse)
async def login(user_data: UserLogin, db=Depends(get_db_session)):
    user = db.query(User).filter(User.email == user_data.email, User.password == user_data.password).first()
    
    if user:
        return {
            "status": "success",
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "role": user.role
            }
        }
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")