import asyncclick as click

from database import database
from manager.user import UserManager
from models.enums import RoleType


@click.command()
@click.option("-e", "--email", type=str, required=True)
@click.option("-f", "--firstname", type=str, required=True)
@click.option("-l", "--lastname", type=str, required=True)
@click.option("-pa", "--password", type=str, required=True)
@click.option("-p", "--phone", type=str, required=True)
@click.option("-i", "--iban", type=str, required=True)
async def create_super_user(email, firstname, lastname, password, phone, iban):
    user_data = {
        "email": email, "firstname": firstname, "lastname": lastname,
        "password": password, "phone": phone, "iban": iban, "role": RoleType.admin
    }
    await database.connect()
    await UserManager.register(user_data)
    await database.connect()


if __name__ == "__main__":
    create_super_user(_anyio_backend="asyncio")
