from datetime import datetime, timedelta
from jose import jwt
from jose import JWTError
from fastapi import HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {
            "exp": expire
        }
    )

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )

        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
def get_current_user(token: str = Depends(oauth2_scheme)):

    username = verify_token(token)

    return username    