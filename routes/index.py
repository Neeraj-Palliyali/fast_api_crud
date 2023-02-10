from fastapi import APIRouter
import conn
from models.user import users
from schema.queries import Query
from schema.mutations import Mutation
import strawberry
from strawberry.asgi import GraphQL


user = APIRouter()
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

user.add_route("/graphql", graphql_app)
