from pydantic import BaseModel

from models import RoleType


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


class UserOut(BaseUser):
    id: int
    firstname: str
    lastname: str
    phone: str
    role: RoleType
    iban: str
