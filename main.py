from fastapi import FastAPI
from routes import urls

app = FastAPI()

app.include_router(urls)