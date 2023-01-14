import os
from typing import Any

import dotenv

dotenv.load_dotenv()


def get_var(key: str, default: Any = None) -> int | str:
    try:
        return os.environ[key]
    except KeyError:
        if default:
            return default
        raise Exception("%s not found" % key)


DB_NAME: str = str(get_var("DB_NAME"))
DB_USER: str = str(get_var("DB_USER"))
DB_PASSWORD: str = str(get_var("DB_PASSWORD"))
DB_HOST: str = str(get_var("DB_HOST"))
DB_PORT: int = int(get_var("DB_PORT"))

API_PORT: int = int(get_var("API_PORT", 8000))

SECRET_KEY: str = str(get_var("SECRET_KEY"))
DEBUG: bool = bool(int(get_var("DEBUG", 1)))

JWT_ALG: str = str(get_var("JWT_ALG", "HS256"))
