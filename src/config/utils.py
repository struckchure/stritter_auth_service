import typing
import uuid
from datetime import datetime, timedelta

import bcrypt
from jose import JWTError, jwt

from config import env
from props.user_props import TokensObject


class Token:
    @staticmethod
    def create_access_token(
        data: dict, expires_in: timedelta = timedelta(days=7)
    ) -> str:
        return jwt.encode(
            {"exp": datetime.now() + expires_in, **data},
            key=env.SECRET_KEY,
            algorithm=env.JWT_ALG,
        )

    @staticmethod
    def create_refresh_token(
        data: dict, expires_in: timedelta = timedelta(days=10)
    ) -> str:
        return jwt.encode(
            {"exp": datetime.now() + expires_in, **data},
            key=env.SECRET_KEY,
            algorithm=env.JWT_ALG,
        )

    @staticmethod
    def generate_token(data) -> TokensObject:
        return {
            "access": Token.create_access_token(data),
            "refresh": Token.create_refresh_token(data),
        }

    @staticmethod
    def decode_token(token) -> dict[str, typing.Any | uuid.UUID]:
        try:
            alg = jwt.get_unverified_headers(token)["alg"]
            return jwt.decode(token, key=env.SECRET_KEY, algorithms=alg)
        except JWTError as e:
            raise e
        except Exception as e:
            raise e


class Encryption:
    @staticmethod
    def hash_password(password: str) -> bytes:
        return bcrypt.hashpw(bytes(password, "utf-8"), bcrypt.gensalt())

    @staticmethod
    def check_password(password: str, hashed: str) -> bool:
        return bcrypt.checkpw(bytes(password, "utf-8"), bytes(hashed, "utf-8"))
