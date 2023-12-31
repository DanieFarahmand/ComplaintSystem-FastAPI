from datetime import datetime, timedelta
from typing import Optional

import jwt
from decouple import config
from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from starlette.requests import Request

from database import database
from models import RoleType
from models.user import User


class AuthManager:

    @staticmethod
    def encode_token(user):
        try:
            payload = {
                "sub": user.id,
                "exp": datetime.utcnow() + timedelta(minutes=120)
            }
            return jwt.encode(payload, config("SECRET_KEY"), algorithm="HS256")
        except Exception as ex:
            raise ex


class CustomHttpBearer(HTTPBearer):

    async def __call__(
            self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        res = await super().__call__(request)

        try:
            payload = jwt.decode(res.credentials, config("SECRET_KEY"), algorithms=["HS256"])
            user_data = await database.fetch_one(select(User).where(User.id == payload["sub"]))
            request.state.user = user_data
            return user_data

        except jwt.ExpiredSignatureError:
            raise HTTPException(401, "Token has expired")

        except jwt.InvalidTokenError:
            raise HTTPException(401, "Invalid token")


oauth2_scheme = CustomHttpBearer()


def is_complainer(request: Request):
    if not request.state.user.role == RoleType.complainer.name:
        raise HTTPException(403, "Forbidden")


def is_approver(request: Request):
    if not request.state.user.role == RoleType.approver.name:
        raise HTTPException(403, "Forbidden")


def is_admin(request: Request):
    if not request.state.user.role == RoleType.admin.name:
        raise HTTPException(403, "Forbidden")
