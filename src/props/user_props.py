import typing
import uuid

import pydantic


class TokensObject(typing.TypedDict):

    access: str
    refresh: str


class UserObject(typing.TypedDict, total=False):

    id: uuid.UUID
    first_name: str
    last_name: str
    username: str
    email: str
    tokens: TokensObject


class UserProps(pydantic.BaseModel):

    first_name: typing.Optional[str]
    last_name: typing.Optional[str]
    username: pydantic.constr(to_lower=True)  # type: ignore
    email: typing.Optional[str]
    password: str | bytes


class UserRegisterProps(UserProps):

    password: pydantic.constr(min_length=6)  # type: ignore


class UserLoginProps(pydantic.BaseModel):

    username: pydantic.constr(to_lower=True, min_length=2)  # type: ignore
    password: pydantic.constr(min_length=6)  # type: ignore


class UserUpdateProps(UserRegisterProps):

    username: typing.Optional[pydantic.constr(to_lower=True, min_length=2)]  # type: ignore
    password: typing.Optional[pydantic.constr(min_length=6)]  # type: ignore
