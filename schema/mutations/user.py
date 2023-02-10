import strawberry
from conn.db import conn
from models.user import users


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, name: str, email: str, password: str) -> bool:
        result = conn.execute(users.insert().values(
            name=name,
            email=email,
            password=password
        ))
        print(result)
        return int(result.inserted_primary_key[0])

    @strawberry.mutation
    def update_user(self, info, id: int, name: str, email: str, password: str) -> str:
        result = conn.execute(users.insert().values(
            name=name,
            email=email,
            password=password
        ))
        return str(result.rowcount) + "'s rows affected"

    @strawberry.mutation
    def delete_user(self, info, id: int) -> bool:
        result = conn.execute(users.delete().where(users.c.id == id))
        return result.rowcount > 0
