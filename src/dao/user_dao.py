import uuid

import peewee

from config.db import db
from models.user_model import UserModel
from props.user_props import UserProps, UserUpdateProps


class UserDAO:
    @staticmethod
    def create_user(user_data: UserProps) -> UserModel:
        with db.atomic():
            try:
                return UserModel.create(**user_data.dict(exclude_none=True))
            except peewee.IntegrityError as e:
                raise Exception("User already exist")

    @staticmethod
    def get_user(user_id: uuid.UUID) -> UserModel:
        try:
            return UserModel.get_by_id(user_id)
        except peewee.DoesNotExist:
            raise Exception("User does not exist")

    @staticmethod
    def get_user_by_username(username: str) -> UserModel:
        try:
            return UserModel.get(UserModel.username == username)
        except peewee.DoesNotExist:
            raise Exception("User does not exist")

    @staticmethod
    def update_user(user_id: uuid.UUID, user_data: UserUpdateProps) -> int:
        with db.atomic():
            try:
                return (
                    UserModel.update(**user_data.dict(exclude_none=True))
                    .where(UserModel.id == user_id)
                    .execute()
                )
            except Exception as error:
                raise Exception(str(error))

    @staticmethod
    def delete_user(user_id: uuid.UUID) -> None:
        with db.atomic():
            try:
                UserModel.delete_by_id(user_id)
            except Exception as error:
                raise Exception(str(error))
