from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy import insert, select
from asyncpg import UniqueViolationError

from database import database
from models.user import User
from manager.auth import AuthManager

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserManager:
    @staticmethod
    async def register(user_data):
        user_data["password"] = pwd_context.hash(user_data["password"])
        try:
            id_ = await database.execute(insert(User).values(**user_data))
        except UniqueViolationError:
            raise HTTPException(400, "User with this email is already exists")
        user = await database.fetch_one(select(User).where(User.id == id_))
        return AuthManager.encode_token(user)

    @staticmethod
    async def login(user_data):
        user = await database.fetch_one(select(User).where(User.email == user_data["email"]))
        if not user:
            raise HTTPException(400, "Wrong email or password")
        elif not pwd_context.verify(user_data["password"], user["password"]):
            raise HTTPException(400, "Wrong email or password")
        return AuthManager.encode_token(user)