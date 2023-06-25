from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str


class UserRegisterIn(BaseUser):
    firstname: str
    lastname: str
    password: str
    phone: str
    iban: str
    role: str


class UserLoginIn(BaseUser):
    password: str
