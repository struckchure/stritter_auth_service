import peewee

from config.db import BaseModel


class UserModel(BaseModel):

    first_name = peewee.CharField(max_length=50, null=True)
    last_name = peewee.CharField(max_length=50, null=True)
    username = peewee.CharField(max_length=50, unique=True)
    email = peewee.CharField(max_length=50, null=True)
    password = peewee.CharField(max_length=100)

    class Meta:
        table_name = "users"
