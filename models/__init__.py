from conn.db import engine, meta
from .user import users

meta.create_all(engine)
