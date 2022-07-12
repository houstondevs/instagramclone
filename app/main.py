from fastapi import FastAPI

from app.routes.users.routes import router as user_router
from app.routes.posts.posts import router as post_router
from app.db.db import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(post_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
