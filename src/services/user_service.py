import uuid

from fastapi.exceptions import HTTPException

from config.utils import Encryption, Token
from dao.user_dao import UserDAO, UserProps
from props.user_props import UserObject, UserUpdateProps


class UserService:
    @staticmethod
    def register_user(
        username: str,
        password: str,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
    ) -> UserObject:
        try:
            user = UserDAO.create_user(
                user_data=UserProps(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=Encryption.hash_password(password),
                )
            )
        except Exception as error:
            raise HTTPException(status_code=400, detail=str(error))

        return UserObject(
            **{
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "email": user.email,
                "tokens": Token.generate_token({"user_id": str(user.id)}),
            }
        )

    @staticmethod
    def login_user(username: str, password: str) -> UserObject:
        try:
            user = UserDAO.get_user_by_username(username=username)
        except Exception as error:
            raise HTTPException(status_code=403, detail=str(error))

        if not Encryption.check_password(password, str(user.password)):
            raise HTTPException(status_code=403, detail="Invalid credentials")

        return UserObject(
            **{
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "email": user.email,
                "tokens": Token.generate_token({"user_id": str(user.id)}),
            }
        )

    @staticmethod
    def get_user(user_id: uuid.UUID) -> UserObject:
        try:
            user = UserDAO.get_user(user_id=user_id)

            return UserObject(
                **{
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                    "email": user.email,
                }
            )
        except Exception as error:
            raise HTTPException(status_code=403, detail=str(error))

    @staticmethod
    def update_user(
        user_id: uuid.UUID,
        username: str | None = None,
        password: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
    ) -> UserObject:
        try:
            UserDAO.update_user(
                user_id=user_id,
                user_data=UserUpdateProps(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=Encryption.hash_password(password) if password else None,  # type: ignore
                ),
            )

            user = UserDAO.get_user(user_id=user_id)

            return UserObject(
                **{
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                    "email": user.email,
                    "tokens": Token.generate_token({"user_id": str(user.id)}),
                }
            )
        except Exception as error:
            raise HTTPException(status_code=403, detail=str(error))
