from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.schemas import RegisterSchema, LoginSchema
from app.services import register_user, login_user
from app.security import verify_token

router = APIRouter()

# AUTH ROUTES
@router.post("/register")
def register(data: RegisterSchema):
    return register_user(data)

@router.post("/login")
def login(data: LoginSchema):
    return login_user(data)

# JWT PROTECTION
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    return payload

# TEST PROTECTED
@router.get("/protected")
def protected(user=Depends(get_current_user)):
    return {"message": "You are authorized", "user": user}