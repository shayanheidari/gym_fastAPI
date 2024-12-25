from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import users


Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(users.router)


@app.get("/")
def root() -> dict:
    message: dict = {
        "message": "hello this is the gym program! please sign in."}
    return message
