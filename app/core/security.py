import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

TOKEN_LIVE_TIME = 15
SECRET_KEY = "your-super-secret-key-for-jwt-do-not-share"
ALGORITH = "HS256"
security = HTTPBearer()

def hash_password(password: str, cost_factor: int = 12)-> str:
    password_byte = password.encode("utf-8")
    salt = bcrypt.gensalt(rounds=cost_factor)
    hashed_password = bcrypt.hashpw(password_byte,salt)

    return hashed_password.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str)-> bool:
    password_bytes = plain_password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def create_access_token(data: dict)->str:
    to_encode = data.copy()

    expire = datetime.now(timezone.utc)+timedelta(minutes= TOKEN_LIVE_TIME)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITH)

    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm = [ALGORITH])
        return payload
    
    except jwt.ExpiredSignatureError:
         raise HTTPException(
            status_code=401,
            detail="Token has expired"
        )
    
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    payload = decode_access_token(token)

    username = payload.get("sub")

    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    return username