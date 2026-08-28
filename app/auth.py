"""
Authentication and JWT security utilities for the FastAPI application.

This module provides JWT token creation, token verification,
and retrieval of the currently authenticated user.
"""

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
    """
    Create a JWT access token with an expiration time.

    Args:
        data: Payload data to encode into the JWT.

    Returns:
        str: Encoded JWT access token.
    """

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
    """
    Verify and decode a JWT access token.

    Args:
        token: JWT access token received from the client.

    Returns:
        str: Username stored in the token subject.

    Raises:
        HTTPException: If the token is invalid or does not contain
            a username.
    """

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
    """
    Retrieve the authenticated username from the JWT token.

    Args:
        token: Bearer token provided through FastAPI's OAuth2
            security dependency.

    Returns:
        str: Authenticated username.
    """

    username = verify_token(token)

    return username