import strawberry
from typing import List
from conn import conn
from ..type.user import User
from models import users


@strawberry.type
class Query:
    @strawberry.field
    def get_user(self, info, id: int) -> User:

        return conn.execute(
            users.select().where(users.c.id == id)).first()

    @strawberry.field
    def get_all_users(self, info) -> List[User]:
        return conn.execute(
            users.select()).fetchall()
