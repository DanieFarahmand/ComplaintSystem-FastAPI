from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from models.enums import RoleType

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(128), unique=True)
    firstname = Column(String(128))
    lastname = Column(String(128))
    password = Column(String(128))
    phone = Column(String(20))
    iban = Column(String(34))
    role = Column(Enum(RoleType), nullable=False, server_default=RoleType.complainer.name)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
