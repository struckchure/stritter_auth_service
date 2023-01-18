import uuid

from fastapi import APIRouter, Depends, Query

from config.dependencies import CommonHeaderProps, common_headers
from props.user_props import (
    UserLoginProps,
    UserObject,
    UserRegisterProps,
    UserUpdateProps,
)
from services.user_service import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/register/")
def register_user_api(user_data: UserRegisterProps) -> UserObject:
    return UserService.register_user(**user_data.dict(exclude_none=True))


@router.post("/login/")
def login_user_api(user_creds: UserLoginProps) -> UserObject:
    return UserService.login_user(**user_creds.dict(exclude_none=True))


@router.get("/profile/")
def get_user_profile_api(
    commons: CommonHeaderProps = Depends(common_headers),
) -> UserObject:
    return UserService.get_user(user_id=commons.user_id)


@router.put("/profile/")
def update_user_profile_api(
    user_data: UserUpdateProps, commons: CommonHeaderProps = Depends(common_headers)
) -> UserObject:
    return UserService.update_user(
        user_id=commons.user_id, **user_data.dict(exclude_none=True)
    )


@router.get("/")
def get_users_by_id_api(user_ids: list[uuid.UUID] = Query(None)) -> list[UserObject]:
    return list(map(UserService.get_user, user_ids)) if user_ids else []
