from fastapi import FastAPI

from app.db.db import init_db
from app.routes.users.routes import router as user_router
from app.routes.posts.posts import router as post_router

app = FastAPI()

app.include_router(user_router)
app.include_router(post_router)


@app.on_event("startup")
async def startup():
    await init_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}
