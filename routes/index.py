from fastapi import APIRouter
from conn import conn
from models.user import users
from schema.queries import Query
import strawberry
from strawberry.asgi import GraphQL


user = APIRouter()
schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

user.add_route("/graphql", graphql_app)
