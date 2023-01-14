import uuid

import peewee

from config import env

db = peewee.PostgresqlDatabase(
    env.DB_NAME,
    user=env.DB_USER,
    password=env.DB_PASSWORD,
    host=env.DB_HOST,
    port=env.DB_PORT,
)


class BaseModel(peewee.Model):

    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        database = db
