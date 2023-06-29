from fastapi import APIRouter, Depends
from typing import Optional

from manager.auth import oauth2_scheme, is_admin
from manager.user import UserManager

router = APIRouter(tags=["Users"])


@router.get("/users/", dependencies=[Depends(oauth2_scheme), Depends(is_admin)])
async def get_users(email: Optional[str] = None):
    if email:
        return await UserManager.get_user_by_email(email)
    return await UserManager.get_all_users()
