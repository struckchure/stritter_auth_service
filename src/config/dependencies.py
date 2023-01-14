import uuid

import pydantic
from fastapi import Header

from config.utils import Token


class CommonHeaderProps(pydantic.BaseModel):
    user_id: uuid.UUID


async def common_headers(Authorization: str = Header()) -> CommonHeaderProps:
    return CommonHeaderProps(
        user_id=Token.decode_token(Authorization.split(" ")[1])["user_id"]
    )
